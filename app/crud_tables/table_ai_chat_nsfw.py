from __future__ import annotations

import json
from typing import Any

from app.ai_chat.models import (
    MediaAsset,
    MediaKind,
    MediaSafetySource,
    MediaSafetyStatus,
)
from app.ai_chat.nsfw_types import NSFWScanResult, NSFWScanStatus, NSFWVerdict
from app.crud_tables.table_ai_chat_helpers import parse_execute_count, row_get
from app.crud_tables.table_ai_chat_media import media_asset_from_row


def _media_kind_value(kind: MediaKind | str) -> str:
    pass  # TODO: Commercial logic


def _scan_job_status_for_result(result: NSFWScanResult) -> NSFWScanStatus:
    pass  # TODO: Commercial logic


class AIChatNSFWTable:
    def __init__(self, db):
        pass  # TODO: Commercial logic

    async def fetch_pending_media_assets_without_scan_jobs(
        self,
        *,
        limit: int = 500,
    ) -> list[MediaAsset]:
        pass  # TODO: Commercial logic

    async def create_nsfw_scan_job(
        self,
        asset: MediaAsset,
        *,
        priority: int = 100,
        max_attempts: int = 3,
    ) -> int | None:
        pass  # TODO: Commercial logic

    async def claim_nsfw_scan_jobs(
        self,
        *,
        worker_id: str,
        limit: int = 5,
        lock_seconds: int = 300,
    ) -> list[Any]:
        pass  # TODO: Commercial logic

    async def mark_nsfw_scan_job_done(self, *, job_id: int) -> int:
        pass  # TODO: Commercial logic

    async def mark_nsfw_scan_job_failed(
        self,
        *,
        job_id: int,
        error_text: str,
        retry: bool = True,
        retry_delay_seconds: int = 300,
        terminal_reason: str = "nsfw_scan_failed",
    ) -> int:
        pass  # TODO: Commercial logic

    async def fetch_nsfw_scan_cache(
        self,
        *,
        file_unique_id: str,
        kind: MediaKind | str,
        provider: str,
        model_name: str,
    ):
        pass  # TODO: Commercial logic

    async def fetch_media_scan_evidence(
        self,
        *,
        chat_id: int,
        file_unique_id: str,
        kind: MediaKind | str,
    ):
        pass  # TODO: Commercial logic

    async def upsert_nsfw_scan_cache(
        self,
        *,
        file_unique_id: str,
        kind: MediaKind | str,
        provider: str,
        model_name: str,
        safety_status: MediaSafetyStatus,
        safety_reason: str,
        scores: dict[str, Any] | None = None,
        model_version: str | None = None,
        max_pornography_score: float | None = None,
        max_hentai_score: float | None = None,
        max_sensual_score: float | None = None,
        frames_checked: int = 0,
        content_hash: str | None = None,
        phash: str | None = None,
        error: str | None = None,
    ) -> None:
        pass  # TODO: Commercial logic

    async def apply_nsfw_scan_result(
        self,
        *,
        asset_id: int,
        result: NSFWScanResult,
        job_id: int | None = None,
    ) -> int:
        pass  # TODO: Commercial logic
