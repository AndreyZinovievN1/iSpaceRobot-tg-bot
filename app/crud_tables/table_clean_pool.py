"""Служебные таблицы пула юзерботов ежедневной уборки.

Пул — это несколько независимых аккаунтов Telegram (роли ``cleaner``,
``cleaner2``, ``cleaner3`` ...), которые заходят в группы и остаются там.
Чтобы это не превратилось в хаос, нужны три вещи, которые нельзя держать в
памяти процесса:

* ``clean_pool_groups`` — за каким аккаунтом закреплена группа, состоит ли он
  в ней, когда последний раз проверяли и какая у группы ссылка/юзернейм;
* ``clean_pool_joins`` — сколько входов сделал аккаунт за сутки (дневной
  лимит должен переживать перезапуск бота);
* ``clean_pool_members`` — кого аккаунт реально видел в живых группах. Это
  самое сильное доказательство «аккаунт жив»: если мы видели пользователя в
  группе, удалять его из БД нельзя.

Все функции намеренно «мягкие»: при любой ошибке БД они возвращают
``None``/``False`` и пишут предупреждение, но НЕ бросают исключение. Уборка
из-за сбоя служебной таблицы падать не должна. Вход в группы при недоступной
таблице запрещается на уровне пула: без учёта лимитов и закреплений входить
нельзя.
"""

from __future__ import annotations

import time
from typing import Any, Dict, Iterable, List, Optional, Sequence

from config import logger
from app.db import db

__all__ = [
    "ensure_pool_schema",
    "schema_ready",
    "get_assignment",
    "set_assignment",
    "save_reference",
    "mark_member",
    "mark_state",
    "touch_checked",
    "count_memberships",
    "membership_counts",
    "joins_today",
    "bump_joins",
    "save_members",
    "alive_user_ids",
    "snapshot_candidates",
    "mark_snapshot_done",
]

#: Состояния закрепления группы за аккаунтом:
#: ``pending`` — закреплена, но членство не подтверждено;
#: ``member`` — аккаунт состоит в группе;
#: ``requested`` — отправлена заявка на вступление (админ должен одобрить);
#: ``failed`` — войти не удалось (лимит, приватность, запрет).
_STATE_MEMBER = "member"

#: DDL выполняется отдельными запросами: asyncpg не умеет несколько
#: команд в одном ``execute`` при подготовленном выражении.
_SCHEMA_STATEMENTS: Sequence[str] = (
    """
    CREATE TABLE IF NOT EXISTS clean_pool_groups (
        group_id BIGINT PRIMARY KEY,
        role TEXT NOT NULL,
        state TEXT NOT NULL DEFAULT 'pending',
        title TEXT,
        username TEXT,
        invite_link TEXT,
        participants INTEGER,
        last_error TEXT,
        joined_at TIMESTAMPTZ,
        snapshot_at TIMESTAMPTZ,
        checked_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
        updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
    )
    """,
    """
    CREATE INDEX IF NOT EXISTS clean_pool_groups_role_state_idx
        ON clean_pool_groups (role, state)
    """,
    """
    CREATE TABLE IF NOT EXISTS clean_pool_joins (
        role TEXT NOT NULL,
        day DATE NOT NULL,
        joins INTEGER NOT NULL DEFAULT 0,
        PRIMARY KEY (role, day)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS clean_pool_members (
        user_id BIGINT NOT NULL,
        group_id BIGINT NOT NULL,
        role TEXT NOT NULL,
        seen_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
        PRIMARY KEY (user_id, group_id)
    )
    """,
    """
    CREATE INDEX IF NOT EXISTS clean_pool_members_seen_idx
        ON clean_pool_members (seen_at)
    """,
    """
    CREATE INDEX IF NOT EXISTS clean_pool_members_user_idx
        ON clean_pool_members (user_id)
    """,
)

#: ``None`` — ещё не проверяли; True/False — результат последней проверки.
_schema_ready: Optional[bool] = None
_schema_checked_at: float = 0.0
#: Как часто пробовать снова, если БД была недоступна (секунды).
_SCHEMA_RETRY_SECONDS = 600.0


async def ensure_pool_schema(force: bool = False) -> bool:
    """Создаёт служебные таблицы пула (идемпотентно).

    Возвращает ``True``, если таблицами можно пользоваться. При ошибке
    возвращает ``False`` и повторяет попытку не чаще раза в 10 минут, чтобы
    недоступная БД не забивала лог на каждой проверке чата.
    """
    pass  # TODO: Commercial logic


def schema_ready() -> bool:
    """Быстрая проверка без обращения к БД (для отчёта)."""
    pass  # TODO: Commercial logic


async def _fetchrow(query: str, *args: Any) -> Optional[Dict[str, Any]]:
    pass  # TODO: Commercial logic


async def _execute(query: str, *args: Any) -> bool:
    pass  # TODO: Commercial logic



# --------------------------------------------------------------------------- #
#                        ЗАКРЕПЛЕНИЕ ГРУППЫ ЗА АККАУНТОМ                      #
# --------------------------------------------------------------------------- #
async def get_assignment(group_id: int) -> Optional[Dict[str, Any]]:
    """Текущая запись группы в пуле (роль, состояние, ссылки)."""
    pass  # TODO: Commercial logic


async def set_assignment(group_id: int, role: str) -> Optional[str]:
    """Закрепляет группу за аккаунтом. Существующее закрепление не меняет.

    Возвращает РЕАЛЬНУЮ роль закрепления: если группа уже была закреплена за
    другим аккаунтом, вернётся она — так при добавлении нового аккаунта
    старые группы не «переезжают» и не приходится входить дважды.
    """
    pass  # TODO: Commercial logic


async def save_reference(
    group_id: int,
    role: str,
    *,
    title: Optional[str] = None,
    username: Optional[str] = None,
    invite_link: Optional[str] = None,
    participants: Optional[int] = None,
) -> None:
    """Запоминает название/юзернейм/ссылку группы, пока бот ещё в ней.

    Это «страховка на будущее»: если бота из группы уберут, у пула останется
    чем проверить существование группы, не входя в неё.
    """
    pass  # TODO: Commercial logic



async def mark_member(
    group_id: int,
    role: str,
    *,
    title: Optional[str] = None,
    username: Optional[str] = None,
    invite_link: Optional[str] = None,
    participants: Optional[int] = None,
) -> None:
    """Фиксирует, что аккаунт точно состоит в группе."""
    pass  # TODO: Commercial logic


async def mark_state(
    group_id: int,
    role: str,
    state: str,
    *,
    error: Optional[str] = None,
) -> None:
    """Меняет состояние закрепления, но НИКОГДА не разжаловывает ``member``.

    Понижение ``member`` → ``failed`` опасно: аккаунт остаётся в группе, а
    учёт начинает считать его «не входящим» и снова пытается войти. Поэтому
    подтверждённое членство перезаписывается только другим ``member``.
    """
    pass  # TODO: Commercial logic


async def touch_checked(group_id: int) -> None:
    """Отмечает время последней успешной проверки группы."""
    pass  # TODO: Commercial logic


# --------------------------------------------------------------------------- #
#                              ЛИМИТЫ И СТАТИСТИКА                            #
# --------------------------------------------------------------------------- #
async def count_memberships(role: str) -> Optional[int]:
    """Сколько групп закреплено за аккаунтом как «состоит».

    ``None`` = посчитать не удалось. Вызывающая сторона обязана трактовать
    это как «лимит неизвестен» и НЕ входить в новые группы.
    """
    pass  # TODO: Commercial logic


async def membership_counts() -> Dict[str, int]:
    """Членство по ролям — для отчёта (пустой словарь при ошибке)."""
    pass  # TODO: Commercial logic


async def joins_today(role: str) -> Optional[int]:
    """Сколько входов аккаунт уже сделал сегодня (``None`` = не знаем)."""
    pass  # TODO: Commercial logic


async def bump_joins(role: str) -> None:
    """Увеличивает дневной счётчик входов аккаунта."""
    pass  # TODO: Commercial logic


# --------------------------------------------------------------------------- #
#                         СНИМОК УЧАСТНИКОВ (ЖИВЫЕ)                          #
# --------------------------------------------------------------------------- #
async def save_members(
    role: str,
    group_id: int,
    user_ids: Iterable[int],
) -> int:
    """Сохраняет участников группы. Возвращает число записанных строк.

    Снимок используется как доказательство «аккаунт жив»: если мы видели
    пользователя в живой группе, удалять его из БД нельзя. Поэтому пишем
    только реально полученных пользователей (никаких «пустых» записей).
    """
    pass  # TODO: Commercial logic


async def alive_user_ids(
    user_ids: Sequence[int],
    days: int,
) -> set:
    """Кого из списка мы видели в живых группах за последние ``days`` дней."""
    pass  # TODO: Commercial logic


async def snapshot_candidates(role: str, limit: int, days: int) -> List[int]:
    """Группы аккаунта, где снимок участников пора обновить."""
    pass  # TODO: Commercial logic


async def mark_snapshot_done(group_id: int) -> None:
    """Отмечает, что снимок участников группы обновлён."""
    pass  # TODO: Commercial logic
