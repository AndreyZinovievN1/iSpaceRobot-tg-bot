import re
import time
import uuid
import html
import traceback
from collections import defaultdict, Counter

try:
    import psutil
except Exception:
    psutil = None


class DebugHub:
    IGNORE_ERROR_PATTERNS = (
        "message is not modified",
        "message can't be edited",
        "query is too old",
        "message to delete not found",
        "message to edit not found",
    )

    IGNORE_CONSOLE_PATTERNS = (
        "telegram server says - flood control exceeded",
        "retry in ",
        "retry after ",
        "telegramretryafter",
        "message is not modified",
        "message can't be edited",
        "query is too old",
        "message to delete not found",
        "message to edit not found",
    )

    def __init__(self, config, notifier):
        pass  # TODO: Commercial logic

    def _reset_interval_stats(self):
        pass  # TODO: Commercial logic

    def _cleanup_trace_db_events(self, max_items: int = 50):
        pass  # TODO: Commercial logic

    def new_trace_id(self) -> str:
        pass  # TODO: Commercial logic

    def _escape(self, value) -> str:
        pass  # TODO: Commercial logic

    def _code(self, value) -> str:
        pass  # TODO: Commercial logic

    def _pre(self, value) -> str:
        pass  # TODO: Commercial logic

    def _normalize_command(self, command_text: str | None, event_type: str) -> str:
        pass  # TODO: Commercial logic

    def _get_status(self, current_stats: dict) -> str:
        pass  # TODO: Commercial logic

    def _format_top_list(self, title: str, counter: Counter, limit: int = 3, max_name: int = 120) -> str:
        pass  # TODO: Commercial logic

    def _extract_retry_after_seconds(self, error: Exception) -> int | None:
        pass  # TODO: Commercial logic

    def _format_seconds_human(self, seconds: int | None) -> str:
        pass  # TODO: Commercial logic

    def _trim_text(self, text: str, limit: int = 1200, from_end: bool = False) -> str:
        pass  # TODO: Commercial logic

    def _trim_traceback_tail(self, text: str, max_lines: int = 25, max_chars: int = 2500) -> str:
        pass  # TODO: Commercial logic

    def _short_file_path(self, path: str) -> str:
        pass  # TODO: Commercial logic

    def _extract_traceback_info(self, error: Exception) -> dict:
        pass  # TODO: Commercial logic

    def _is_minor_error(self, text: str) -> bool:
        pass  # TODO: Commercial logic

    def _should_skip_console_error(self, text: str) -> bool:
        pass  # TODO: Commercial logic

    def _clean_error_text(self, text: str) -> str:
        pass  # TODO: Commercial logic

    def _compact_error_text(self, text: str, limit: int = 500) -> str:
        pass  # TODO: Commercial logic

    def _compact_console_text(self, text: str, limit: int = 350) -> str:
        pass  # TODO: Commercial logic

    def _top_error_key(self, err_name: str, err_text: str) -> str:
        pass  # TODO: Commercial logic

    def _get_ram_mb(self) -> float | None:
        pass  # TODO: Commercial logic

    async def _send_minor_or_skip(self, title: str, body: str) -> bool:
        pass  # TODO: Commercial logic

    async def capture_slow_update(
        self,
        *,
        trace_id: str,
        event_type: str,
        command_text: str | None,
        user_id: int | None,
        chat_id: int | None,
        duration_ms: float,
    ):
        pass  # TODO: Commercial logic

    async def capture_exception(
        self,
        *,
        trace_id: str,
        event_type: str,
        user_id: int | None,
        chat_id: int | None,
        command_text: str | None,
        error: Exception,
        duration_ms: float,
    ):
        pass  # TODO: Commercial logic

    async def capture_db(
        self,
        *,
        trace_id: str | None,
        source: str,
        query: str,
        acquire_ms: float,
        sql_ms: float,
        user_id: int | None,
        chat_id: int | None,
    ):
        pass  # TODO: Commercial logic

    async def capture_tg_api(
        self,
        *,
        trace_id: str | None,
        method: str,
        source: str,
        duration_ms: float,
        target_chat_id: int | None,
        user_id: int | None,
        chat_id: int | None,
        extra: dict | None = None,
    ):
        pass  # TODO: Commercial logic

    async def capture_tg_api_error(
        self,
        *,
        trace_id: str | None,
        method: str,
        source: str,
        duration_ms: float,
        target_chat_id: int | None,
        user_id: int | None,
        chat_id: int | None,
        error: Exception,
        extra: dict | None = None,
    ):
        pass  # TODO: Commercial logic

    async def capture_console_error(self, *, source: str, text: str):
        pass  # TODO: Commercial logic

    async def capture_asyncio_error(
        self,
        *,
        text: str,
        message: str | None = None,
        source: str | None = None,
    ):
        pass  # TODO: Commercial logic

    async def send_summary(self):
        pass  # TODO: Commercial logic
