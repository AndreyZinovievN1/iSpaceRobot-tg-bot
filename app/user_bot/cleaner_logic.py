"""
Ежедневная очистка БД Space 5.1 (юзербот + бот).

Модуль удаляет из базы только заведомо мёртвые сущности:

* чаты из таблицы ``settings`` — чаты, которые удалены/недоступны и в которых
  бот физически не может работать;
* пользователей из таблицы ``users`` — аккаунты, удалённые в Telegram
  (флаг ``deleted`` — 13-й бит ``UserFlags`` от Telegram, он же
  ``pyrogram.types.User.is_deleted``).

Главный принцип — «лучше оставить, чем удалить лишнее»:

1. Каждый кандидат проверяется ``DAILY_CLEAN_*_CONFIRMATIONS`` раз ПОДРЯД
   (минимум 2). Удаляется только то, что подтвердилось во ВСЕХ проверках.
2. Чаты проверяются двумя независимыми источниками: бот (``get_chat`` +
   ``get_chat_member``) и юзербот (``get_chat``). Если юзербот видит чат —
   это «бот вылетел», а не «чат мёртв».
3. Пользователи удаляются ТОЛЬКО по явному флагу ``deleted`` от Telegram либо
   при совпадении двух независимых признаков: юзербот получил именно
   ``UserEmpty`` И бот видит строгую заглушку «Deleted Account» без username.
   Отсутствие ответа юзербота, FloodWait, таймауты, ошибки прав и
   «chat not found» НЕ считаются доказательством смерти аккаунта.
4. Дополнительный предохранитель: если кандидатов на удаление больше
   ``DAILY_CLEAN_MAX_DELETE_PERCENT`` (по умолчанию 10%) от числа проверенных,
   этап аккаунтов останавливается и не удаляет НИЧЕГО.
5. Есть сухой прогон (dry-run) — ничего не удаляется и не меняется в БД,
   только отчёт.
6. Если юзербот недоступен, пользователи не удаляются вообще.
7. Никогда не удаляются владелец и админы бота.

Все действия, причины и спорные случаи логируются в лог-чат (``log_group``).
"""

from __future__ import annotations

import asyncio
import os
import time
from dataclasses import dataclass, field, replace
from datetime import datetime
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple

from pytz import timezone as _pytz_timezone

from aiogram.exceptions import (
    TelegramBadRequest,
    TelegramForbiddenError,
    TelegramNetworkError,
    TelegramNotFound,
    TelegramRetryAfter,
    TelegramServerError,
)

try:  # pyrogram обязателен, но импорт защищён, чтобы бот не падал целиком
    from pyrogram import Client, raw
    from pyrogram.errors import FloodWait, RPCError

    PYROGRAM_AVAILABLE = True
    _PYROGRAM_IMPORT_ERROR: Optional[str] = None
except Exception as _pyrogram_error:  # noqa: BLE001
    Client = None  # type: ignore[assignment]

    class _MissingPyrogram(Exception):
        pass

    class FloodWait(_MissingPyrogram):  # type: ignore[no-redef]
        value = 0

    class RPCError(_MissingPyrogram):  # type: ignore[no-redef]
        pass

    class _MissingRaw:
        class types:  # type: ignore[no-redef]
            InputUser = object

        class functions:  # type: ignore[no-redef]
            class users:  # type: ignore[no-redef]
                GetUsers = object

    raw = _MissingRaw  # type: ignore[assignment]
    PYROGRAM_AVAILABLE = False
    _PYROGRAM_IMPORT_ERROR = str(_pyrogram_error)

from config import OWNER_ID, bot, logger
from app.db import db
from app.user_bot import userbot_manager
from app.user_bot.cleaner_pool import CleanPool, PoolProbe, parse_accounts
from app.crud_tables.table_log_group import get_log_group_id
from app.crud_tables.table_settings import get_settings_by_group_id, remove_settings
from app.crud_tables.table_users import (
    fetch_admin_chat_ids,
    fetch_users_for_cleanup,
    mark_users_cleaned,
    remove_user,
    remove_user_in_private_only,
    update_full_name,
    update_username,
)

__all__ = [
    "CleanConfig",
    "CleanReport",
    "run_daily_clean",
    "start_userbot",
    "stop_userbot",
    "get_userbot",
    "parse_clean_mode",
    "is_running",
    "last_report",
    "LOG_THREAD_ID",
]

# Тред в лог-чате, куда сыпем отчёты (как в остальных командах проекта)
LOG_THREAD_ID = 434078
MSK_TZ = _pytz_timezone("Europe/Moscow")


# --------------------------------------------------------------------------- #
#                      ЧТЕНИЕ НАСТРОЕК ИЗ ОКРУЖЕНИЯ                            #
# --------------------------------------------------------------------------- #
def _env_str(name: str, default: Optional[str] = None) -> Optional[str]:
    pass  # TODO: Commercial logic


def _env_bool(name: str, default: bool) -> bool:
    pass  # TODO: Commercial logic


def _env_int(
    name: str,
    default: int,
    *,
    minimum: int = 0,
    maximum: Optional[int] = None,
) -> int:
    pass  # TODO: Commercial logic


def _env_float(name: str, default: float, *, minimum: float = 0.0) -> float:
    pass  # TODO: Commercial logic


def _format_msk(timestamp: Optional[float]) -> str:
    """Время в МСК для отчётов (пустая строка, если времени ещё нет)."""
    pass  # TODO: Commercial logic


def _now_msk() -> str:
    pass  # TODO: Commercial logic


def _mass_delete_percent(checked: int, candidates: int) -> float:
    """Доля кандидатов на удаление от числа реально проверенных."""
    pass  # TODO: Commercial logic


def _mass_delete_guard(cfg: "CleanConfig", checked: int, candidates: int) -> bool:
    """Сработал ли предохранитель от массового удаления."""
    pass  # TODO: Commercial logic


@dataclass
class CleanConfig:
    """Настройки прогона очистки (все ключи переопределяются через .env)."""

    thread_id: Optional[int] = LOG_THREAD_ID

    # --- чаты ---
    chats_enabled: bool = True
    group_delay: float = 1.2
    group_confirmations: int = 2
    remove_dead_chats: bool = True
    remove_kicked_chats: bool = False
    # Абсолютный потолок удалений за один прогон. Даже если проценты «в норме»,
    # больше этого числа записей за раз не удаляется: ошибка в проверке не
    # должна снести половину базы.
    max_delete_chats: int = 50

    # --- пул юзерботов (несколько аккаунтов «зашли и остались») ---
    pool_enabled: bool = True
    pool_accounts_raw: str = "1"
    pool_accounts: Tuple[int, ...] = (1,)
    pool_join: bool = True
    pool_join_in_dry_run: bool = False
    pool_join_channels: bool = False
    pool_join_per_run: int = 10
    pool_join_per_day: int = 30
    pool_join_delay: float = 45.0
    pool_join_flood_max: float = 300.0
    pool_lookup_flood_max: float = 120.0
    pool_max_memberships: int = 400
    pool_membership_recheck_days: int = 7
    pool_snapshot: int = 200
    pool_snapshot_days: int = 7
    pool_snapshot_groups_per_run: int = 10
    pool_alive_days: int = 30
    pool_cross_check_accounts: int = 3
    #: Удалять «мёртвый» чат только если пул реально смог его проверить.
    #: Если пул недоступен/не проверил — запись остаётся.
    dead_require_pool: bool = True
    #: Просить у бота ссылку-приглашение, пока он ещё в группе. Без неё
    #: закрытую группу нельзя проверить после вылета бота (и нельзя войти).
    capture_invites: bool = True
    profile_bio: Optional[str] = None
    profile_first_name: Optional[str] = None
    profile_last_name: Optional[str] = None

    # --- пользователи ---
    users_enabled: bool = True
    user_batch: int = 100
    user_delay: float = 1.5
    user_confirmations: int = 2
    confirm_delay: float = 4.0
    max_users: int = 5000
    inactive_days: int = 90
    update_profiles: bool = True
    purge_private: bool = True
    # Абсолютный потолок удалений аккаунтов за прогон (в дополнение к проценту).
    max_delete_users: int = 50

    # --- общее ---
    dry_run: bool = False
    # Исторический флаг. False больше НЕ включает удаление по косвенным
    # признакам: без явного подтверждения аккаунт всегда остаётся.
    require_proof: bool = True
    # Предохранитель от массового удаления: если кандидатов на удаление больше
    # указанного процента от проверенных, этап аккаунтов останавливается и НИЧЕГО
    # не удаляет. 0 = предохранитель выключен (не рекомендуется).
    max_delete_percent: float = 10.0
    call_timeout: float = 30.0
    progress_every: int = 25
    detail_flush: int = 12
    log_working: bool = False

    @classmethod
    def from_env(cls) -> "CleanConfig":
        pass  # TODO: Commercial logic


@dataclass
class CleanReport:
    """Итоги прогона: используется для отчёта в лог-чат."""

    trigger: str = "auto"
    dry_run: bool = False
    started_at: float = field(default_factory=time.time)
    finished_at: Optional[float] = None

    chats_total: int = 0
    chats_working: int = 0
    chats_kicked: int = 0
    chats_dead: int = 0
    chats_unknown: int = 0
    chats_removed: int = 0
    chats_delete_failed: int = 0

    users_total: int = 0
    users_checked: int = 0
    users_working: int = 0
    users_deleted: int = 0
    users_unknown: int = 0
    users_removed: int = 0
    users_delete_failed: int = 0
    users_vetoed: int = 0
    profiles_updated: int = 0

    flood_waits: int = 0
    errors: int = 0
    userbot_used: bool = False
    skipped_reason: Optional[str] = None

    # --- пул юзерботов ---
    pool_accounts: int = 0
    pool_members: int = 0
    pool_joined: int = 0
    pool_resolved: int = 0
    pool_not_found: int = 0
    pool_skipped: int = 0
    pool_snapshots: int = 0
    pool_snapshot_users: int = 0
    pool_join_block: Optional[str] = None
    #: Сколько удалений аккаунтов отменило вето «пул видел его живым».
    users_alive_veto: int = 0

    @property
    def duration(self) -> float:
        pass  # TODO: Commercial logic

    @property
    def duration_human(self) -> str:
        pass  # TODO: Commercial logic



# --------------------------------------------------------------------------- #
#                      ЮЗЕРБОТ УБОРКИ (РОЛЬ "CLEANER")                          #
# --------------------------------------------------------------------------- #
# Клиенты и сессии живут в app/user_bot/userbot_manager.py. Уборка пользуется
# ТОЛЬКО ролью "cleaner": подарки/Mini App поднимают отдельный аккаунт
# ("gifts"), поэтому прогон уборки и запросы мини-приложения больше не делят
# одну сессию Pyrogram и не ломают друг другу TL-слой.
def userbot_session_path() -> str:
    """Путь к файлу сессии уборки без расширения."""
    pass  # TODO: Commercial logic


SESSION_LOCK_PAUSE = userbot_manager.SESSION_LOCK_PAUSE
_is_lock_error = userbot_manager._is_lock_error
_tune_session_db = userbot_manager._tune_session_db
_release_client = userbot_manager._release_client


def get_userbot() -> Optional["Client"]:
    """Возвращает подключённый юзербот уборки или None."""
    pass  # TODO: Commercial logic


def userbot_last_error() -> Optional[str]:
    """Последняя ошибка запуска юзербота уборки (для ``/health``)."""
    pass  # TODO: Commercial logic


async def start_userbot() -> Optional["Client"]:
    """Лениво поднимает юзербот уборки (роль ``cleaner``)."""
    pass  # TODO: Commercial logic


async def stop_userbot() -> None:
    """Аккуратно гасит юзербот уборки и закрывает его файл сессии."""
    pass  # TODO: Commercial logic


# --------------------------------------------------------------------------- #
#                    БЕЗОПАСНЫЕ ВЫЗОВЫ (FLOOD / TIMEOUT)                       #
# --------------------------------------------------------------------------- #
_RETRY_LIMIT = 4


async def _bot_call(
    factory: Callable[[], Any],
    cfg: CleanConfig,
    label: str,
    report: Optional[CleanReport] = None,
) -> Any:
    """Вызов aiogram-бота с обработкой FloodWait (429) и сетевых сбоев."""
    pass  # TODO: Commercial logic


async def _ubot_call(
    factory: Callable[[], Any],
    cfg: CleanConfig,
    label: str,
    report: Optional[CleanReport] = None,
) -> Any:
    """Вызов pyrogram-юзербота с обработкой FloodWait и сетевых сбоев."""
    pass  # TODO: Commercial logic



# --------------------------------------------------------------------------- #
#                        КЛАССИФИКАЦИЯ ОШИБОК TELEGRAM                         #
# --------------------------------------------------------------------------- #
_NOT_FOUND_MARKERS = (
    "chat not found",
    "user not found",
    "peer_id_invalid",
    "user_id_invalid",
    "chat_id_invalid",
    "channel_invalid",
    "bot was blocked",
    "deactivated",
    "not found",
)
_KICKED_MARKERS = (
    "kicked",
    "not a member",
    "member list is inaccessible",
    "chat_write_forbidden",
    "no rights",
    "not enough rights",
    "bot is not a member",
)
_ALIVE_MEMBER_STATUSES = {"creator", "administrator", "member", "restricted"}
_UBOT_NOT_FOUND_MARKERS = (
    "peer_id_invalid",
    "peer id invalid",
    "user not found",
    "chat not found",
    "chat_id_invalid",
    "chat id invalid",
)


def _is_ubot_not_found(exc: BaseException) -> bool:
    """Похоже ли исключение юзербота на «объекта нет», а не на сбой связи.

    FloodWait/таймауты/сетевые ошибки НЕЛЬЗЯ считать доказательством смерти
    чата: иначе один сбой превращается в удаление живой записи.
    """
    pass  # TODO: Commercial logic


def classify_bot_error(exc: BaseException) -> str:
    """Грубая классификация ошибки Telegram: not_found | kicked | forbidden | other."""
    pass  # TODO: Commercial logic


@dataclass
class ChatVerdict:
    """Результат проверки одного чата из таблицы settings."""

    group_id: int
    status: str = "unknown"  # working | kicked | dead | unknown
    reason: str = ""
    title: Optional[str] = None
    bot_sees: bool = False
    userbot_sees: bool = False
    bot_error: Optional[str] = None
    userbot_error: Optional[str] = None
    #: Бот ответил именно «чата нет» (404/not found), а не сбоем связи.
    bot_not_found: bool = False
    #: Данные группы, которые бот видит, пока он ещё в чате. Нужны, чтобы
    #: потом проверить существование группы без входа (юзернейм/ссылка).
    username: Optional[str] = None
    invite_link: Optional[str] = None
    participants: Optional[int] = None

    # --- чем помог пул юзерботов ---
    pool_state: Optional[str] = None
    pool_role: Optional[str] = None
    pool_joined: bool = False
    pool_reason: Optional[str] = None

    @property
    def destroys_settings(self) -> bool:
        """True, если запись чата должна быть убрана из settings."""
        pass  # TODO: Commercial logic


async def evaluate_chat(
    group_id: int,
    cfg: CleanConfig,
    report: Optional[CleanReport] = None,
    pool: Optional["CleanPool"] = None,
) -> ChatVerdict:
    """Проверяет чат ботом, а при сомнениях — ещё и пулом юзерботов.

    Пул — независимый свидетель: он состоит в группах и видит их изнутри.
    Его ответ НЕ может ухудшить вердикт: он способен только превратить
    «мёртвый» чат в «вылет бота» (тогда запись остаётся) и добавить группу в
    пул. Если пул не смог проверить — вердикт становится «неизвестно», а не
    «мёртвый».
    """
    pass  # TODO: Commercial logic


async def _export_invite(
    group_id: int,
    cfg: CleanConfig,
    report: Optional[CleanReport],
) -> Optional[str]:
    """Ссылка-приглашение от бота (нужна пулу, чтобы войти в закрытую группу).

    Требует прав администратора с «приглашать пользователей». Любая ошибка —
    просто ``None``: без ссылки уборка работает как раньше.
    """
    pass  # TODO: Commercial logic


async def _pool_step(
    verdict: ChatVerdict,
    cfg: CleanConfig,
    report: Optional[CleanReport],
    pool: "CleanPool",
) -> Optional[PoolProbe]:
    """Спрашивает пул о чате. Никогда не бросает исключение."""
    pass  # TODO: Commercial logic


def _decide_after_pool(
    verdict: ChatVerdict,
    probe: Optional[PoolProbe],
    cfg: CleanConfig,
) -> ChatVerdict:
    """Итоговый вердикт, когда бот чат не видит.

    «Мёртвым» чат становится только если пул реально проверил группу и тоже
    её не увидел. Любая неопределённость пула — запись остаётся.
    """
    pass  # TODO: Commercial logic


async def _legacy_ubot_step(
    verdict: ChatVerdict,
    cfg: CleanConfig,
    report: Optional[CleanReport],
) -> ChatVerdict:
    """Старая проверка одиночным юзерботом (когда пул выключен)."""
    pass  # TODO: Commercial logic



# --------------------------------------------------------------------------- #
#                          ЛОГИРОВАНИЕ В АДМИН-ЧАТ                             #
# --------------------------------------------------------------------------- #
def _is_thread_error(exc: BaseException) -> bool:
    """Ошибка отправки именно в тему форума, а не сетевой сбой."""
    pass  # TODO: Commercial logic


def _split_chunks(text: str, limit: int) -> List[str]:
    """Режет длинный текст на куски по границам блоков (по 2 перевода строки)."""
    pass  # TODO: Commercial logic


class CleanReporter:
    """Пишет отчёт в лог-чат: главное сообщение-прогресс + пачки деталей."""

    MAX_MESSAGE_LEN = 3500

    def __init__(self, log_group_id: Optional[int], cfg: CleanConfig):
        pass  # TODO: Commercial logic

    @property
    def enabled(self) -> bool:
        pass  # TODO: Commercial logic

    async def _send(self, text: str):
        pass  # TODO: Commercial logic

    async def start(self, text: str) -> None:
        pass  # TODO: Commercial logic

    async def notify(self, text: str) -> None:
        pass  # TODO: Commercial logic

    async def detail(self, text: str) -> None:
        pass  # TODO: Commercial logic

    async def flush(self) -> None:
        pass  # TODO: Commercial logic

    async def progress(self, text: str, *, force: bool = False) -> None:
        pass  # TODO: Commercial logic

    async def finish(self, text: str) -> None:
        pass  # TODO: Commercial logic



# --------------------------------------------------------------------------- #
#                              ЭТАП 1: ЧАТЫ                                    #
# --------------------------------------------------------------------------- #
async def _clean_chats(
    cfg: CleanConfig,
    report: CleanReport,
    reporter: CleanReporter,
    pool: Optional["CleanPool"] = None,
) -> None:
    """Убирает из settings чаты, в которых бот больше не может работать."""
    pass  # TODO: Commercial logic



async def _chat_mass_delete_guard(
    cfg: CleanConfig,
    report: CleanReport,
    reporter: CleanReporter,
    to_delete: int,
) -> bool:
    """Останавливает удаление чатов, если оно выглядит массовым.

    Два независимых предохранителя:

    * доля от проверенных больше ``DAILY_CLEAN_MAX_DELETE_PERCENT``;
    * абсолютное число больше ``DAILY_CLEAN_MAX_DELETE_CHATS``.

    Срабатывание любого = в этом прогоне не удаляется НИ ОДИН чат. Лучше
    оставить мёртвые записи до следующего раза, чем снести рабочие настройки
    из-за ошибки в проверке.
    """
    pass  # TODO: Commercial logic


async def _confirm_and_remove_chats(
    candidates: List[ChatVerdict],
    cfg: CleanConfig,
    report: CleanReport,
    reporter: CleanReporter,
    pool: Optional["CleanPool"] = None,
) -> None:
    """Подтверждает кандидатов несколькими проверками и удаляет записи."""
    pass  # TODO: Commercial logic



# --------------------------------------------------------------------------- #
#                          ЭТАП 2: ПОЛЬЗОВАТЕЛИ                               #
# --------------------------------------------------------------------------- #
def _user_entry_raw(item: Any) -> Dict[str, Any]:
    """Достаёт из raw-объекта Telegram данные, нужные для решения и лога."""
    pass  # TODO: Commercial logic


def _user_entry_parsed(user: Any) -> Dict[str, Any]:
    """То же самое, но для pyrogram-объекта User (fallback-путь)."""
    pass  # TODO: Commercial logic


async def fetch_users_info(
    ubot: "Client",
    user_ids: Sequence[int],
    cfg: CleanConfig,
    report: Optional[CleanReport] = None,
) -> Dict[int, Dict[str, Any]]:
    """Пакетно тянет информацию о пользователях у Telegram через юзербот.

    Возвращает словарь ``{user_id: {...}}`` ТОЛЬКО для id, которые Telegram
    реально вернул. Отсутствие id в ответе = «не знаю», а не «удалён».
    """
    pass  # TODO: Commercial logic


def _looks_like_deleted_account_name(name: Any, username: Any) -> bool:
    """Очень строгая проверка заглушки Telegram.

    Раньше здесь было сравнение по подстроке ``deleted``: живой человек с именем
    «Deleted» мог попасть под удаление. Теперь принимаем только точное название
    заглушки и только если у неё нет username (у удалённых аккаунтов его нет).
    """
    pass  # TODO: Commercial logic


async def _check_user_by_bot(
    user_id: int,
    cfg: CleanConfig,
    report: Optional[CleanReport] = None,
) -> Dict[str, Any]:
    """Перекрёстная проверка аккаунта обычным ботом.

    ``status``: working | deleted | not_found | unknown.
    """
    pass  # TODO: Commercial logic


@dataclass
class UserVerdict:
    """Результат проверки одного пользователя из таблицы users."""

    chat_id: int
    status: str = "unknown"  # working | deleted | unknown
    reason: str = ""
    name: Optional[str] = None
    username: Optional[str] = None
    db_name: Optional[str] = None
    db_username: Optional[str] = None
    last_activity: Any = None
    userbot_said: str = ""
    bot_said: str = ""

    @property
    def title(self) -> str:
        pass  # TODO: Commercial logic



async def evaluate_user(
    user_id: int,
    cfg: CleanConfig,
    report: Optional[CleanReport] = None,
    row: Optional[Dict[str, Any]] = None,
    ubot_info: Optional[Dict[str, Any]] = None,
    ubot: Optional["Client"] = None,
    known_alive: bool = False,
) -> UserVerdict:
    """Проверяет одного пользователя по двум независимым источникам.

    Удаляем ТОЛЬКО при явном подтверждении Telegram (флаг ``deleted``),
    либо при совпадении двух независимых признаков: юзербот не получил
    профиль (``UserEmpty``) И бот видит заглушку удалённого аккаунта.
    Любая неопределённость = запись остаётся жить.
    """
    pass  # TODO: Commercial logic



async def _protected_user_ids() -> Optional[set]:
    """ID, которые нельзя удалять: админы, бот, владелец, лог-чат.

    ``None`` — список админов получить не удалось. В этом случае удаление
    запрещено: нельзя чистить базу, не зная, кто неприкосновенен.
    """
    pass  # TODO: Commercial logic


async def _pool_alive_ids(pool: Optional["CleanPool"], user_ids: Sequence[int]) -> set:
    """Кого пул видел в живых группах. При сбое — пустое множество.

    Пустое множество здесь безопасно: оно означает «вето не сработало», а не
    «все мертвы». Удаление всё равно требует подтверждения из Telegram.
    """
    pass  # TODO: Commercial logic


async def _user_alive_in_pool(pool: Optional["CleanPool"], user_id: int) -> bool:
    """Финальная проверка перед удалением: пул видел аккаунт живым?"""
    pass  # TODO: Commercial logic


async def _clean_users(
    cfg: CleanConfig,
    report: CleanReport,
    reporter: CleanReporter,
    ubot: "Client",
    pool: Optional["CleanPool"] = None,
) -> None:
    """Проверяет аккаунты из таблицы users и убирает удалённые."""
    pass  # TODO: Commercial logic



async def _update_user_profile(
    verdict: UserVerdict,
    cfg: CleanConfig,
    report: CleanReport,
) -> None:
    """Подтягивает в БД свежие имя/юзернейм живого аккаунта."""
    pass  # TODO: Commercial logic


async def _confirm_and_remove_users(
    candidates: List[UserVerdict],
    cfg: CleanConfig,
    report: CleanReport,
    reporter: CleanReporter,
    ubot: "Client",
    pool: Optional["CleanPool"] = None,
) -> None:
    """Подтверждает удалённые аккаунты повторными проверками и чистит БД."""
    pass  # TODO: Commercial logic



# --------------------------------------------------------------------------- #
#                        ФОРМИРОВАНИЕ ТЕКСТОВ ОТЧЁТА                           #
# --------------------------------------------------------------------------- #
def _stage_icon(cfg: CleanConfig, report: CleanReport) -> str:
    pass  # TODO: Commercial logic


def _main_text(
    cfg: CleanConfig,
    report: CleanReport,
    status: Optional[str],
    *,
    final: bool = False,
) -> str:
    """Короткая «шапка», которую редактируем по ходу прогона."""
    pass  # TODO: Commercial logic


def _final_text(cfg: CleanConfig, report: CleanReport) -> str:
    pass  # TODO: Commercial logic



# --------------------------------------------------------------------------- #
#                             ТОЧКА ВХОДА                                     #
# --------------------------------------------------------------------------- #
_clean_lock = asyncio.Lock()
_last_report: Optional[CleanReport] = None


def is_running() -> bool:
    """Уборка уже идёт? (защита от двойного запуска)."""
    pass  # TODO: Commercial logic


def last_report() -> Optional[CleanReport]:
    pass  # TODO: Commercial logic


_MODE_ALIASES = {
    "dry": {"dry_run": True},
    "драй": {"dry_run": True},
    "тест": {"dry_run": True},
    "test": {"dry_run": True},
    "chats": {"chats_enabled": True, "users_enabled": False},
    "чаты": {"chats_enabled": True, "users_enabled": False},
    "users": {"users_enabled": True, "chats_enabled": False},
    "юзеры": {"users_enabled": True, "chats_enabled": False},
    "аккаунты": {"users_enabled": True, "chats_enabled": False},
    "all": {"chats_enabled": True, "users_enabled": True},
    "всё": {"chats_enabled": True, "users_enabled": True},
    "все": {"chats_enabled": True, "users_enabled": True},
}


def parse_clean_mode(raw: Optional[str], base: Optional[CleanConfig] = None) -> CleanConfig:
    """Собирает конфиг из аргументов команды ``!очистка ...``.

    Доступные слова: ``dry``/``драй``/``тест``, ``chats``/``чаты``,
    ``users``/``юзеры``/``аккаунты``, ``all``/``всё``.
    Неизвестное слово включает dry-run, чтобы опечатка не запустила удаление.
    """
    pass  # TODO: Commercial logic


async def run_daily_clean(
    config: Optional[CleanConfig] = None,
    trigger: str = "auto",
) -> Optional[CleanReport]:
    """Полный прогон ежедневной уборки. Возвращает отчёт (или None, если занято)."""
    pass  # TODO: Commercial logic
