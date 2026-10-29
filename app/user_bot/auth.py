"""
Слой совместимости для старого модуля ежедневной уборки.

Вся логика живёт в :mod:`app.user_bot.cleaner_logic`. Этот файл оставлен,
чтобы старые импорты вида::

    from app.user_bot.auth import log_daily_clear

продолжали работать и не падали после рефакторинга (в проекте такие импорты
были в ``main.py`` и ``app/owner/owner_cmds.py``).
"""

from __future__ import annotations

from typing import Any, Optional

from .cleaner_logic import (  # noqa: F401  (реэкспорт публичного API)
    LOG_THREAD_ID,
    CleanConfig,
    CleanReport,
    get_userbot,
    is_running,
    last_report,
    parse_clean_mode,
    run_daily_clean,
    start_userbot,
    stop_userbot,
    userbot_last_error,
)

__all__ = [
    "log_daily_clear",
    "run_daily_clean",
    "parse_clean_mode",
    "start_userbot",
    "stop_userbot",
    "get_userbot",
    "userbot_last_error",
    "is_running",
    "last_report",
    "CleanConfig",
    "CleanReport",
    "LOG_THREAD_ID",
]


async def log_daily_clear(
    app: Optional[Any] = None,
    bot_client: Optional[Any] = None,
    *,
    mode: Optional[str] = None,
) -> Optional[CleanReport]:
    """Устаревшая точка входа: ``await log_daily_clear(user_app, message.bot)``.

    Аргументы оставлены только ради совместимости — юзербот больше не
    передаётся извне, :mod:`cleaner_logic` сам поднимает и переиспользует
    клиент Pyrogram (файл сессии ``USERBOT_SESSION`` или ``USERBOT_SESSION_STRING``).

    Возвращает отчёт о прогоне либо ``None``, если уборка уже выполняется.
    """
    pass  # TODO: Commercial logic
