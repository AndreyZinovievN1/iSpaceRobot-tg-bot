from __future__ import annotations

from typing import Iterable

from app.crud_tables.table_ai_chat_helpers import row_get


class AIChatWordsTable:
    def __init__(self, db):
        pass  # TODO: Commercial logic

    async def fetch_top_chat_words(self, chat_id: int, limit: int = 20) -> list[str]:
        pass  # TODO: Commercial logic

    async def fetch_top_user_words(
        self,
        chat_id: int,
        user_id: int,
        limit: int = 16,
    ) -> list[str]:
        pass  # TODO: Commercial logic

    async def upsert_chat_words(self, chat_id: int, words: Iterable[str]) -> None:
        pass  # TODO: Commercial logic

    async def upsert_user_words(
        self,
        chat_id: int,
        user_id: int,
        words: Iterable[str],
    ) -> None:
        pass  # TODO: Commercial logic
