from __future__ import annotations

import asyncio
import logging
import random
import re
from collections.abc import Iterable
from collections import defaultdict, deque
from dataclasses import dataclass, replace
from typing import Any

from aiogram.exceptions import (
    TelegramBadRequest,
    TelegramForbiddenError,
    TelegramNetworkError,
    TelegramRetryAfter,
)

from app.ai_chat.models import ActionType, MediaAsset, MediaKind, MediaSafetySource, MediaSafetyStatus
from app.ai_chat.nsfw_config import nsfw_scan_enabled
from app.ai_chat.repository import (
    AIChatRepository,
    MEDIA_CATALOG_LIMIT_PER_CHAT,
    MEDIA_SEND_FAILURE_LIMIT,
    row_get,
)
from app.ai_chat.safety_service import (
    approve_media,
    block_media,
    ensure_media_can_be_reused,
    list_approved_media,
    list_blocked_media,
    list_pending_media,
    media_collection_enabled,
    prepare_asset_for_storage,
    reset_media_to_pending,
    validate_provider_scan_evidence,
)


logger = logging.getLogger(__name__)


SAFE_EMOJIS = [
    "👍",
    "❤️",
    "🔥",
    "👏",
    "😁",
    "🤔",
    "🌚",
    "💀",
    "👌",
    "✨",
]
REACTION_EMOJIS = ["👍", "❤️", "🔥", "👏", "😁", "🤔"]
RECENT_MEDIA_LIMIT = 20
MEDIA_FRESH_REUSE_DELAY_SECONDS = 1800
GIF_KINDS = (MediaKind.ANIMATION, MediaKind.DOCUMENT_ANIMATION)
STICKER_KINDS = (MediaKind.STICKER,)
MEDIA_MEME_KINDS = (
    MediaKind.PHOTO,
    MediaKind.VIDEO,
    MediaKind.ANIMATION,
    MediaKind.DOCUMENT_ANIMATION,
)
NSFW_SCANNABLE_MEDIA_KINDS = (
    MediaKind.PHOTO,
    MediaKind.VIDEO,
    MediaKind.ANIMATION,
    MediaKind.DOCUMENT_ANIMATION,
    MediaKind.STICKER,
)

DOCUMENT_ANIMATION_MIME_TYPES = {
    "image/gif",
    "video/mp4",
    "video/webm",
}
DOCUMENT_ANIMATION_SUFFIXES = {".gif", ".mp4", ".webm"}
LEGACY_UNTRUSTED_SAFETY_REASONS = ("auto_approved_no_classifier",)
NSFW_SCAN_REQUIRED_REASON = "nsfw_scan_required"
BROKEN_SEND_REASON = "broken_send_failed"
ASSET_RELATED_BAD_REQUEST_MARKERS = (
    "invalid file_id",
    "wrong file identifier",
    "file_reference_expired",
    "file reference expired",
    "wrong remote file id",
    "failed to get http url content",
)
NON_ASSET_BAD_REQUEST_MARKERS = (
    "not enough rights",
    "chat not found",
    "bot is not a member",
    "have no rights",
    "message thread not found",
    "message to reply not found",
)

EMOJI_ONLY_RE = re.compile(
    r"^[\s\ufe0f\u200d"
    r"\U0001F1E6-\U0001F1FF"
    r"\U0001F300-\U0001FAFF"
    r"\u2600-\u27BF]+$"
)


@dataclass(frozen=True, slots=True)
class MediaLearnResult:
    saved: bool
    reason: str
    asset: MediaAsset | None = None


_RECENT_MEDIA: dict[tuple[int, ActionType], deque[str]] = defaultdict(
    lambda: deque(maxlen=RECENT_MEDIA_LIMIT)
)


def is_emoji_only_text(text: str | None) -> bool:
    pass  # TODO: Commercial logic


def choose_safe_emoji(*, mood_name: str = "normal") -> str:
    pass  # TODO: Commercial logic


def _text_context(message: Any) -> str | None:
    pass  # TODO: Commercial logic


def _file_suffix(file_name: str | None) -> str:
    pass  # TODO: Commercial logic


def _safe_metadata(**items) -> dict[str, Any]:
    pass  # TODO: Commercial logic


def _is_group_message(message: Any) -> bool:
    pass  # TODO: Commercial logic


def _source_metadata(message: Any) -> dict[str, Any]:
    pass  # TODO: Commercial logic


def _with_patch2_metadata(message: Any, **items) -> dict[str, Any]:
    pass  # TODO: Commercial logic


def _is_asset_related_bad_request(exc: Exception) -> bool:
    pass  # TODO: Commercial logic


def _with_existing_safety(asset: MediaAsset, existing: MediaAsset) -> MediaAsset:
    pass  # TODO: Commercial logic


def _asset_requires_nsfw_scan(asset: MediaAsset) -> bool:
    pass  # TODO: Commercial logic


def _with_pending_nsfw_scan(asset: MediaAsset) -> MediaAsset:
    pass  # TODO: Commercial logic


def _asset_from_animation(message: Any, chat_id: int) -> MediaAsset | None:
    pass  # TODO: Commercial logic


def _asset_from_document_animation(message: Any, chat_id: int) -> MediaAsset | None:
    pass  # TODO: Commercial logic


def _asset_from_sticker(message: Any, chat_id: int) -> MediaAsset | None:
    pass  # TODO: Commercial logic


def _asset_from_photo(message: Any, chat_id: int) -> MediaAsset | None:
    pass  # TODO: Commercial logic


def _asset_from_video(message: Any, chat_id: int) -> MediaAsset | None:
    pass  # TODO: Commercial logic


def _assets_from_custom_emoji(message: Any, chat_id: int) -> list[MediaAsset]:
    pass  # TODO: Commercial logic


def extract_media_assets(message: Any) -> list[MediaAsset]:
    pass  # TODO: Commercial logic


def extract_media_asset(message: Any) -> MediaAsset | None:
    pass  # TODO: Commercial logic


async def learn_media_from_message(message: Any, db, *, settings=None) -> MediaLearnResult:
    pass  # TODO: Commercial logic


async def approve_media_file(db, *, chat_id: int, file_id: str) -> int:
    pass  # TODO: Commercial logic


async def block_media_file(db, *, chat_id: int, file_id: str) -> int:
    pass  # TODO: Commercial logic


def _remember_media(chat_id: int, action: ActionType, file_id: str) -> None:
    pass  # TODO: Commercial logic


def remember_media_action(chat_id: int, action: ActionType, file_id: str) -> None:
    pass  # TODO: Commercial logic


def _recent_media(chat_id: int, action: ActionType) -> list[str]:
    pass  # TODO: Commercial logic


async def has_approved_media(db, *, chat_id: int, action: ActionType, settings=None) -> bool:
    pass  # TODO: Commercial logic


async def pick_approved_media(
    db,
    *,
    chat_id: int,
    action: ActionType,
    reuse_cooldown_seconds: int,
    settings=None,
) -> MediaAsset | None:
    pass  # TODO: Commercial logic


async def has_approved_media_for_meme(db, *, chat_id: int, settings=None) -> bool:
    pass  # TODO: Commercial logic


async def pick_approved_media_for_meme(
    db,
    *,
    chat_id: int,
    reuse_cooldown_seconds: int,
    settings=None,
) -> MediaAsset | None:
    pass  # TODO: Commercial logic


async def _record_asset_send_failure(
    repo: AIChatRepository,
    *,
    asset: MediaAsset,
    action: ActionType,
    error: Exception,
    stage=None,
) -> None:
    pass  # TODO: Commercial logic


def _log_non_broken_send_error(
    *,
    chat_id: int,
    action: ActionType,
    stage=None,
    error: Exception,
) -> None:
    pass  # TODO: Commercial logic


async def send_catalog_gif(
    message: Any,
    db,
    *,
    reuse_cooldown_seconds: int = 3600,
    settings=None,
    stage=None,
) -> bool:
    pass  # TODO: Commercial logic


async def send_catalog_sticker(
    message: Any,
    db,
    *,
    reuse_cooldown_seconds: int = 3600,
    settings=None,
    stage=None,
) -> bool:
    pass  # TODO: Commercial logic


async def send_catalog_emoji(message: Any, *, mood_name: str = "normal") -> bool:
    pass  # TODO: Commercial logic


def _custom_reaction_ids(settings) -> list[str]:
    pass  # TODO: Commercial logic


async def _approved_custom_reaction_ids(message: Any, db, settings) -> list[str]:
    pass  # TODO: Commercial logic


async def send_safe_reaction(message: Any, db=None, *, settings=None, mood_name: str = "normal") -> bool:
    pass  # TODO: Commercial logic
