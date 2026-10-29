from __future__ import annotations

from typing import Any


DEFAULT_MEMORY_MAX_MESSAGES = 5000
DEFAULT_MEMORY_RETENTION_DAYS = 180
DEFAULT_LEARNING_LOG_RETENTION_DAYS = 30


def _row_get(row: Any, key: str, default=None):
    pass  # TODO: Commercial logic


class AIChatSettingsTable:
    def __init__(self, db):
        pass  # TODO: Commercial logic

    async def get_settings(self, chat_id: int):
        pass  # TODO: Commercial logic

    async def ensure_settings(self, chat_id: int):
        pass  # TODO: Commercial logic

    async def update_last_action(self, chat_id: int) -> None:
        pass  # TODO: Commercial logic

    async def update_markov_text_action(self, chat_id: int) -> None:
        pass  # TODO: Commercial logic

    async def fetch_idle_candidate_settings(self):
        pass  # TODO: Commercial logic

    async def fetch_memory_retention_settings(self, chat_id: int) -> tuple[int, int, int]:
        pass  # TODO: Commercial logic
