"""Независимые юзерботы Space 5.1: одна задача — один аккаунт Telegram.

Раньше уборка БД и подарки (Mini App) делили один клиент Pyrogram: пока шла
уборка или возврат TL-слоя после запроса подарков, второй сценарий мог
получить чужой слой/сессию и упасть. Теперь у каждой задачи своя роль —
свой клиент, свой файл сессии и свой аккаунт:

* ``cleaner`` — ежедневная уборка БД (``USERBOT_SESSION`` /
  ``USERBOT_SESSION_STRING``);
* ``gifts`` — подарки и Mini App (``GIFTS_USERBOT_SESSION`` /
  ``GIFTS_USERBOT_SESSION_STRING``).

Модуль намеренно не знает, *что* делает роль: он только поднимает, отдаёт и
гасит клиента. Поэтому третья задача добавляется одной строкой — достаточно
зарегистрировать :class:`UserbotRole` и звать :func:`start_client`.

Важно: аккаунты ролей должны быть РАЗНЫМИ. Если две роли указывают на один и
тот же файл сессии или одну строку сессии, запуск блокируется с понятной
ошибкой: Telegram отзывает сессию при входе вторым клиентом, а sqlite-файл
держит только один процесс.
"""

from __future__ import annotations

import asyncio
import hashlib
import os
import sqlite3
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple, Union

try:  # pyrogram обязателен, но импорт защищён, чтобы бот не падал целиком
    from pyrogram import Client

    PYROGRAM_AVAILABLE = True
    _PYROGRAM_IMPORT_ERROR: Optional[str] = None
except Exception as _pyrogram_error:  # noqa: BLE001
    Client = None  # type: ignore[assignment]
    PYROGRAM_AVAILABLE = False
    _PYROGRAM_IMPORT_ERROR = str(_pyrogram_error)

from config import API_HASH, API_ID, logger

__all__ = [
    "UserbotRole",
    "UserbotSlot",
    "CLEANER_ROLE",
    "GIFTS_ROLE",
    "PYROGRAM_AVAILABLE",
    "SESSION_LOCK_PAUSE",
    "register_role",
    "resolve_role",
    "slot_for",
    "get_client",
    "start_client",
    "stop_client",
    "stop_all_userbots",
    "last_error",
    "session_path",
    "status",
    "role_env_names",
]


@dataclass(frozen=True)
class UserbotRole:
    """Описание роли юзербота: имя сессии и «человеческое» название."""

    name: str
    title: str
    session_env: str
    session_string_env: str
    default_session: str
    log_tag: str


#: Ежедневная уборка БД. Историческое имя переменных сохранено, чтобы
#: существующие установки продолжали работать без правок .env.
CLEANER_ROLE = UserbotRole(
    name="cleaner",
    title="Очистка БД",
    session_env="USERBOT_SESSION",
    session_string_env="USERBOT_SESSION_STRING",
    default_session="my_service_account",
    log_tag="[DAILY_CLEAN]",
)

#: Подарки и Mini App. Отдельный аккаунт — отдельная сессия.
GIFTS_ROLE = UserbotRole(
    name="gifts",
    title="Подарки / Mini App",
    session_env="GIFTS_USERBOT_SESSION",
    session_string_env="GIFTS_USERBOT_SESSION_STRING",
    default_session="gifts_service_account",
    log_tag="[GIFTS]",
)

_ROLES: Dict[str, UserbotRole] = {}
_SLOTS: Dict[str, "UserbotSlot"] = {}

#: Пауза между попытками открыть занятый файл сессии.
SESSION_LOCK_PAUSE = 3.0


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


# --------------------------------------------------------------------------- #
#                              РЕЕСТР РОЛЕЙ                                    #
# --------------------------------------------------------------------------- #
def register_role(role: UserbotRole) -> UserbotRole:
    """Регистрирует роль юзербота (идемпотентно)."""
    pass  # TODO: Commercial logic


def resolve_role(role: Union[str, UserbotRole]) -> UserbotRole:
    """Принимает имя роли или :class:`UserbotRole` и возвращает роль."""
    pass  # TODO: Commercial logic


register_role(CLEANER_ROLE)
register_role(GIFTS_ROLE)


# --------------------------------------------------------------------------- #
#                      РАБОТА С ФАЙЛОМ СЕССИИ                                  #
# --------------------------------------------------------------------------- #
def _is_lock_error(exc: BaseException) -> bool:
    """sqlite сообщил, что база занята (``database is locked``)."""
    pass  # TODO: Commercial logic


def _start_error_text(path: str, exc: BaseException, role: UserbotRole) -> str:
    """Понятная причина сбоя запуска юзербота (её видно в ``/health``)."""
    pass  # TODO: Commercial logic


def _tune_session_db(path: str) -> None:
    """Переводит файл сессии в WAL и включает ``busy_timeout``.

    Pyrogram открывает сессию обычным sqlite и сразу пишет в неё
    (``UPDATE version`` + ``VACUUM`` из ``FileStorage.open``). В режиме
    rollback-журнала это означает «база занята» при любом втором подключении к
    тому же файлу: вторая копия бота, зависшая авторизация из
    ``runtime_tmp/make_userbot_session.py``, старый процесс после перезапуска.
    WAL разрешает читателю и писателю работать одновременно, а ``busy_timeout``
    заставляет sqlite подождать вместо мгновенной ошибки. Режим хранится в самом
    файле, поэтому включаем его заранее. Отключается ``USERBOT_SESSION_WAL=false``.
    """
    pass  # TODO: Commercial logic


async def _release_client(client: Optional[Any], tag: str = "[USERBOTS]") -> None:
    """Освобождает клиента Pyrogram ВМЕСТЕ с файлом сессии.

    ``Client.disconnect()`` закрывает sqlite только у подключённого клиента, а у
    отключённого бросает ``ConnectionError``. Поэтому после неудачного
    ``start()`` файл сессии оставался открытым, и все следующие попытки падали
    на «database is locked». Здесь закрываем хранилище напрямую и не бросаем
    исключений — это уборка, а не рабочий путь.
    """
    pass  # TODO: Commercial logic


# --------------------------------------------------------------------------- #
#                              СЛОТ РОЛИ                                       #
# --------------------------------------------------------------------------- #
class UserbotSlot:
    """Клиент одной роли: собственный лок, клиент и последняя ошибка."""

    def __init__(self, role: UserbotRole):
        pass  # TODO: Commercial logic

    # --- состояние ---
    @property
    def last_error(self) -> Optional[str]:
        pass  # TODO: Commercial logic

    def get(self) -> Optional[Any]:
        """Возвращает подключённого клиента или ``None`` (без запуска)."""
        pass  # TODO: Commercial logic

    def is_connected(self) -> bool:
        pass  # TODO: Commercial logic

    # --- настройки ---
    def session_string(self) -> Optional[str]:
        pass  # TODO: Commercial logic

    def session_path(self) -> str:
        """Путь к файлу сессии без расширения."""
        pass  # TODO: Commercial logic

    def _identity(self) -> Tuple[str, str]:
        """Чем роль отличается от других: строка сессии или путь к файлу."""
        pass  # TODO: Commercial logic

    def _conflict(self) -> Optional[str]:
        """Причина, по которой роль нельзя запускать рядом с другой ролью."""
        pass  # TODO: Commercial logic


    # --- жизненный цикл ---
    async def start(self) -> Optional[Any]:
        """Лениво поднимает клиента роли (один раз за процесс)."""
        pass  # TODO: Commercial logic

    async def stop(self) -> None:
        """Аккуратно гасит клиента роли и закрывает файл сессии."""
        pass  # TODO: Commercial logic


def _slot(role: Union[str, UserbotRole] = CLEANER_ROLE) -> UserbotSlot:
    """Слот роли (создаётся при первом обращении)."""
    pass  # TODO: Commercial logic



# --------------------------------------------------------------------------- #
#                           ПУБЛИЧНОЕ API                                      #
# --------------------------------------------------------------------------- #
def slot_for(role: Union[str, UserbotRole] = CLEANER_ROLE) -> UserbotSlot:
    """Слот роли (создаётся при первом обращении)."""
    pass  # TODO: Commercial logic


def get_client(role: Union[str, UserbotRole] = CLEANER_ROLE) -> Optional[Any]:
    """Подключённый клиент роли или ``None`` (без запуска)."""
    pass  # TODO: Commercial logic


async def start_client(role: Union[str, UserbotRole] = CLEANER_ROLE) -> Optional[Any]:
    """Поднимает клиента роли, если он ещё не подключён."""
    pass  # TODO: Commercial logic


async def stop_client(role: Union[str, UserbotRole] = CLEANER_ROLE) -> None:
    """Останавливает клиента роли."""
    pass  # TODO: Commercial logic


async def stop_all_userbots() -> None:
    """Гасит всех юзерботов (вызывается при остановке бота)."""
    pass  # TODO: Commercial logic


def last_error(role: Union[str, UserbotRole] = CLEANER_ROLE) -> Optional[str]:
    """Последняя ошибка запуска роли (для ``/health``), либо ``None``."""
    pass  # TODO: Commercial logic


def session_path(role: Union[str, UserbotRole] = CLEANER_ROLE) -> str:
    """Путь к файлу сессии роли без расширения."""
    pass  # TODO: Commercial logic


def status() -> Dict[str, Dict[str, Any]]:
    """Состояние всех ролей — без секретов и без подключения к Telegram."""
    pass  # TODO: Commercial logic


def role_env_names() -> List[Tuple[str, str, str]]:
    """Все роли и их переменные окружения (для диагностических скриптов)."""
    pass  # TODO: Commercial logic
