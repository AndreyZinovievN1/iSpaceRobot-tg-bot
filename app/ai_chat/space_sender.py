from __future__ import annotations

import logging
import random
from pathlib import Path

from app.ai_chat.media_catalog import (
    has_approved_media_for_meme,
    remember_media_action,
)
from app.ai_chat.models import ActionType
from app.ai_chat.repository import AIChatRepository, row_get
from app.ai_chat.dialogue_pair_service import try_create_dialogue_pair


logger = logging.getLogger(__name__)


SAFE_REACTIONS = [
    "\U0001F44D",
    "\u2764\ufe0f",
    "\U0001F525",
    "\U0001F44F",
    "\U0001F601",
    "\U0001F914",
]

SAFE_STICKERS = [
    # Add only reviewed sticker file_id values here.
]


def has_supported_media(message) -> bool:
    pass  # TODO: Commercial logic


def cleanup_paths(paths) -> None:
    pass  # TODO: Commercial logic


def _telegram_int(value) -> int | None:
    pass  # TODO: Commercial logic


async def save_space_message(
    db,
    chat_id: int,
    text: str,
    *,
    sent_message=None,
    context_message=None,
    reply_to_message_id: int | None = None,
) -> None:
    pass  # TODO: Commercial logic


async def send_space_text(message, db, phrase: str, *, reply: bool | None = None) -> bool:
    pass  # TODO: Commercial logic


async def send_space_reaction(message) -> bool:
    pass  # TODO: Commercial logic


async def _choose_meme_mode(
    message,
    db,
    settings,
    *,
    stage=None,
    exclude_modes: set[str] | frozenset[str] = frozenset(),
) -> str | None:
    pass  # TODO: Commercial logic


async def send_space_meme(message, db, phrase: str, *, settings=None, stage=None) -> bool:
    pass  # TODO: Commercial logic


async def send_space_voice(message, db, phrase: str, *, settings=None, stage=None) -> bool:
    pass  # TODO: Commercial logic


async def send_space_sticker(message, db) -> bool:
    pass  # TODO: Commercial logic
