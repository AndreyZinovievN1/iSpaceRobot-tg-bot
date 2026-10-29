from __future__ import annotations

from app.ai_chat.models import ChatMemory, ChatMessageRecord, UserMemory
from app.crud_tables.table_ai_chat_helpers import row_get


class AIChatMemoryTable:
    def __init__(self, db):
        pass  # TODO: Commercial logic

    async def upsert_chat_memory_saved(self, chat_id: int, reason: str) -> int:
        pass  # TODO: Commercial logic

    async def upsert_chat_memory_skipped(self, chat_id: int, reason: str) -> None:
        pass  # TODO: Commercial logic

    async def upsert_user_memory_saved(self, record: ChatMessageRecord) -> None:
        pass  # TODO: Commercial logic

    async def upsert_user_memory_skipped(
        self,
        chat_id: int,
        user_id: int,
        user_name: str,
        reason: str,
    ) -> None:
        pass  # TODO: Commercial logic

    async def get_chat_memory(self, chat_id: int) -> ChatMemory | None:
        pass  # TODO: Commercial logic

    async def get_user_memory(self, chat_id: int, user_id: int) -> UserMemory | None:
        pass  # TODO: Commercial logic
