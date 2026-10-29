from __future__ import annotations

from typing import Any

from app.ai_chat.corpus.learning import (
    build_user_name,
    check_learning_text,
    get_message_text,
)
from app.ai_chat.models import (
    ChatMessageRecord,
    LearningEventType,
    LearningResult,
    LearningSkipReason,
)
from app.ai_chat.repository import AIChatRepository
from app.ai_chat.dialogue_pair_service import try_create_dialogue_pair


CLEANUP_EVERY_ACCEPTED_MESSAGES = 100


def _chat_id_from_message(message: Any) -> int | None:
    pass  # TODO: Commercial logic


def _chat_type_from_message(message: Any) -> str | None:
    pass  # TODO: Commercial logic


def _user_from_message(message: Any):
    pass  # TODO: Commercial logic


async def _record_skip(
    repo: AIChatRepository,
    *,
    chat_id: int | None,
    user_id: int | None,
    user_name: str | None,
    reason: str,
    text_sample: str | None = None,
) -> None:
    pass  # TODO: Commercial logic


async def learn_from_message(
    message: Any,
    db,
    *,
    save_message: bool = True,
) -> LearningResult:
    pass  # TODO: Commercial logic
