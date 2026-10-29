from __future__ import annotations

import json
from typing import Any

from app.ai_chat.models import LearningEventType
from app.crud_tables.table_ai_chat_helpers import (
    DEFAULT_CLEANUP_BATCH_SIZE,
    parse_execute_count,
)
from app.crud_tables.table_ai_chat_settings import DEFAULT_LEARNING_LOG_RETENTION_DAYS


class AIChatLearningTable:
    def __init__(self, db):
        pass  # TODO: Commercial logic

    async def log_learning_event(
        self,
        *,
        chat_id: int,
        user_id: int | None,
        event_type: LearningEventType,
        reason: str,
        message_id: int | None = None,
        text_sample: str | None = None,
        metadata: dict[str, Any] | None = None,
    ) -> None:
        pass  # TODO: Commercial logic

    async def cleanup_learning_events(
        self,
        chat_id: int,
        *,
        retention_days: int = DEFAULT_LEARNING_LOG_RETENTION_DAYS,
        batch_size: int = DEFAULT_CLEANUP_BATCH_SIZE,
    ) -> int:
        pass  # TODO: Commercial logic
