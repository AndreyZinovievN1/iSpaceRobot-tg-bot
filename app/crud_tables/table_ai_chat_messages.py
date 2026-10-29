from __future__ import annotations

from app.ai_chat.models import ChatMessageRecord, MessageRole
from app.crud_tables.table_ai_chat_settings import (
    DEFAULT_MEMORY_MAX_MESSAGES,
    DEFAULT_MEMORY_RETENTION_DAYS,
)
from app.crud_tables.table_ai_chat_helpers import (
    DEFAULT_CLEANUP_BATCH_SIZE,
    parse_execute_count,
    row_get,
)


class AIChatMessagesTable:
    def __init__(self, db):
        pass  # TODO: Commercial logic

    async def insert_user_message(
        self,
        record: ChatMessageRecord,
        *,
        telegram_message_id: int | None = None,
        reply_to_message_id: int | None = None,
        message_thread_id: int | None = None,
        sender_user_id: int | None = None,
    ) -> int | None:
        pass  # TODO: Commercial logic

    async def insert_space_message(
        self,
        chat_id: int,
        text: str,
        *,
        telegram_message_id: int | None = None,
        reply_to_message_id: int | None = None,
        message_thread_id: int | None = None,
        sender_user_id: int | None = None,
    ) -> int | None:
        pass  # TODO: Commercial logic

    async def fetch_recent_user_messages(
        self,
        chat_id: int,
        limit: int = 40,
    ) -> list[str]:
        pass  # TODO: Commercial logic

    async def fetch_recent_space_messages(
        self,
        chat_id: int,
        limit: int = 30,
    ) -> list[str]:
        pass  # TODO: Commercial logic

    async def fetch_training_texts(self, chat_id: int, limit: int = 2200) -> list[str]:
        pass  # TODO: Commercial logic

    async def count_user_messages(self, chat_id: int) -> int:
        pass  # TODO: Commercial logic

    async def count_recent_user_messages(self, chat_id: int, hours: int = 2) -> int:
        pass  # TODO: Commercial logic

    async def cleanup_chat_messages(
        self,
        chat_id: int,
        *,
        max_messages: int = DEFAULT_MEMORY_MAX_MESSAGES,
        retention_days: int = DEFAULT_MEMORY_RETENTION_DAYS,
        batch_size: int = DEFAULT_CLEANUP_BATCH_SIZE,
    ) -> int:
        pass  # TODO: Commercial logic
