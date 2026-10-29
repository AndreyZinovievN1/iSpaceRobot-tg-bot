from __future__ import annotations

import asyncio
import logging
import math
from dataclasses import dataclass, replace
from typing import Protocol

from app.ai_chat.models import (
    MediaAsset,
    MediaSafetyDecision,
    MediaSafetySource,
    MediaSafetyStatus,
)
from app.ai_chat.nsfw_provider import PROVIDER_NAME
from app.ai_chat.nsfw_cascade_service import (
    CASCADE_MODEL_NAME,
    CASCADE_PROVIDER_NAME,
    MARQO_MODEL_ID,
    OWEN_MODEL_ID,
)
from app.ai_chat.nsfw_config import load_nsfw_cascade_config
from app.ai_chat.nsfw_provider_config import load_nsfw_provider_config, verdict_from_scores
from app.ai_chat.nsfw_types import NSFWVerdict
from app.ai_chat.repository import AIChatRepository, row_get
from app.crud_tables.table_ai_chat_media import normalize_metadata


ALLOW_RULE = "allow"
DENY_RULE = "deny"
PROVIDER_SAFE_REASON = "nsfw_scan_safe"
HENTAI_BORDERLINE_SAFE_REASON = "nsfw_hentai_borderline_verified_safe"
SCAN_EVIDENCE_TIMEOUT_SECONDS = 0.5
logger = logging.getLogger(__name__)


@dataclass(frozen=True, slots=True)
class ClassificationResult:
    status: MediaSafetyStatus
    reason: str
    confidence: float | None = None


class MediaSafetyProvider(Protocol):
    async def classify_media(self, asset: MediaAsset) -> ClassificationResult:
        """Future lightweight interface for an optional local classifier."""


def media_auto_reuse_enabled(settings) -> bool:
    pass  # TODO: Commercial logic


def media_collection_enabled(settings) -> bool:
    pass  # TODO: Commercial logic


async def decide_media_safety(
    db,
    asset: MediaAsset,
    *,
    provider: MediaSafetyProvider | None = None,
) -> MediaSafetyDecision:
    pass  # TODO: Commercial logic


async def apply_safety_decision(
    db,
    asset: MediaAsset,
    decision: MediaSafetyDecision,
) -> MediaAsset:
    pass  # TODO: Commercial logic


async def prepare_asset_for_storage(
    db,
    asset: MediaAsset,
    *,
    provider: MediaSafetyProvider | None = None,
) -> MediaAsset:
    pass  # TODO: Commercial logic


async def ensure_media_can_be_reused(
    db,
    asset: MediaAsset,
    *,
    settings=None,
) -> tuple[bool, MediaSafetyDecision]:
    pass  # TODO: Commercial logic


def _pending_decision(reason: str) -> MediaSafetyDecision:
    pass  # TODO: Commercial logic


def _blocked_decision(reason: str) -> MediaSafetyDecision:
    pass  # TODO: Commercial logic


def _cascade_pending(reason: str) -> MediaSafetyDecision:
    pass  # TODO: Commercial logic


def _valid_revision(value) -> bool:
    pass  # TODO: Commercial logic


def _validate_cascade_scan_evidence(
    asset: MediaAsset,
    evidence,
    metadata: dict,
) -> MediaSafetyDecision:
    pass  # TODO: Commercial logic


async def validate_provider_scan_evidence(db, asset: MediaAsset) -> MediaSafetyDecision:
    pass  # TODO: Commercial logic


async def approve_media(
    db,
    *,
    chat_id: int,
    file_id: str | None = None,
    file_unique_id: str | None = None,
    reason: str = "manual_approved",
    decided_by_user_id: int | None = None,
) -> int:
    pass  # TODO: Commercial logic


async def block_media(
    db,
    *,
    chat_id: int,
    file_id: str | None = None,
    file_unique_id: str | None = None,
    reason: str = "manual_blocked",
    decided_by_user_id: int | None = None,
) -> int:
    pass  # TODO: Commercial logic


async def reset_media_to_pending(
    db,
    *,
    chat_id: int,
    file_id: str | None = None,
    file_unique_id: str | None = None,
    reason: str = "manual_reset_to_pending",
    decided_by_user_id: int | None = None,
) -> int:
    pass  # TODO: Commercial logic


async def list_pending_media(db, *, chat_id: int, limit: int = 50) -> list[MediaAsset]:
    pass  # TODO: Commercial logic


async def list_blocked_media(db, *, chat_id: int, limit: int = 50) -> list[MediaAsset]:
    pass  # TODO: Commercial logic


async def list_approved_media(db, *, chat_id: int, limit: int = 50) -> list[MediaAsset]:
    pass  # TODO: Commercial logic
