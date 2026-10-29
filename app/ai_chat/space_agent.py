import logging
import re
from dataclasses import dataclass
from typing import Any

from aiogram.types import Message

from app.ai_chat.corpus.learning import check_learning_text
from app.ai_chat.decision_policy import (
    decide_reaction_action,
    decide_chat_action,
    format_decision_log,
    get_chat_stage,
    is_novel_phrase,
    record_successful_action,
)
from app.ai_chat.filters import is_safe_phrase
from app.ai_chat.media_catalog import (
    has_approved_media,
    is_emoji_only_text,
    learn_media_from_message,
    send_catalog_emoji,
    send_catalog_gif,
    send_catalog_sticker,
    send_safe_reaction,
)
from app.ai_chat.memory_service import learn_from_message
from app.ai_chat.models import ActionType
from app.ai_chat.repository import AIChatRepository, row_get
from app.ai_chat.space_generator import generate_space_phrase
from app.ai_chat.space_mood import detect_mood
from app.ai_chat.space_sender import send_space_meme, send_space_text, send_space_voice
from app.ai_chat.style import apply_space_style
from app.ai_chat.voice_engine import is_voice_available


logger = logging.getLogger(__name__)


def _shadow_emit(event: str, fields: dict[str, object]) -> None:
    pass  # TODO: Commercial logic


def _safe_shadow_metric(event: str, **fields: object) -> None:
    pass  # TODO: Commercial logic


def _text_form_flags(text: str | None) -> tuple[bool, bool, bool]:
    pass  # TODO: Commercial logic


def _question_history_metrics(messages: list[str]) -> tuple[bool, int]:
    pass  # TODO: Commercial logic


def _log_shadow_text_form(
    chat_id: int,
    *,
    source_text: str | None,
    selected_text: str | None,
    recent_space_messages: list[str],
) -> None:
    pass  # TODO: Commercial logic


def _log_shadow_outcome(
    chat_id: int | None,
    *,
    silence_reason: str,
    detail_reason: str,
    action: ActionType = ActionType.NOTHING,
    stage=None,
) -> None:
    pass  # TODO: Commercial logic


@dataclass(frozen=True, slots=True)
class AgentDiagnosticReport:
    chat_id: int | None
    action: ActionType
    should_reply: bool
    reason: str
    phrase: str | None = None
    log: str | None = None
    messages_count: int = 0


def get_message_text(message: Message) -> str:
    pass  # TODO: Commercial logic


def has_supported_media(message: Message) -> bool:
    pass  # TODO: Commercial logic


def is_bad_text(text: str) -> bool:
    pass  # TODO: Commercial logic


async def save_user_message(message: Message, db) -> None:
    pass  # TODO: Commercial logic


async def ensure_agent_settings(db, chat_id: int):
    pass  # TODO: Commercial logic


async def get_recent_messages(db, chat_id: int, limit: int = 40) -> list[str]:
    pass  # TODO: Commercial logic


async def count_messages(db, chat_id: int) -> int:
    pass  # TODO: Commercial logic


async def update_last_action(db, chat_id: int) -> None:
    pass  # TODO: Commercial logic


async def _safe_get_memory(repo: AIChatRepository, chat_id: int, user_id: int):
    pass  # TODO: Commercial logic


async def _safe_get_keywords(repo: AIChatRepository, chat_id: int, user_id: int) -> list[str]:
    pass  # TODO: Commercial logic


def _stage_value(stage) -> str | None:
    pass  # TODO: Commercial logic


def _log_media_availability(
    *,
    chat_id: int,
    action: ActionType,
    reason: str,
    stage=None,
    level: int = logging.DEBUG,
) -> None:
    pass  # TODO: Commercial logic


def _voice_log_reason(reason: str) -> str:
    pass  # TODO: Commercial logic


async def _available_actions(db, chat_id: int, settings, *, stage=None) -> set[ActionType]:
    pass  # TODO: Commercial logic


def _log_skip(chat_id: int, reason: str, *, extra: Any = None) -> None:
    pass  # TODO: Commercial logic


def _log_decision(*, chat_id: int, decision, messages_count: int) -> None:
    pass  # TODO: Commercial logic


def _log_generation_outcome(
    chat_id: int,
    *,
    style_applied: bool = False,
    style_novelty_rejected: bool = False,
    final_outcome: str,
) -> None:
    pass  # TODO: Commercial logic


async def _safe_get_recent_space_messages(
    repo: AIChatRepository,
    chat_id: int,
    *,
    limit: int = 30,
) -> list[str]:
    pass  # TODO: Commercial logic


def _is_novel_with_persistent_history(
    chat_id: int,
    phrase: str | None,
    *,
    recent_messages: list[str],
    recent_space_messages: list[str],
) -> bool:
    pass  # TODO: Commercial logic


async def run_space_agent(
    message: Message,
    db,
    *,
    force: bool = False,
    save_message: bool = True,
) -> bool:
    pass  # TODO: Commercial logic


async def diagnose_space_agent(
    message: Message,
    db,
    *,
    force: bool = False,
) -> AgentDiagnosticReport:
    pass  # TODO: Commercial logic
