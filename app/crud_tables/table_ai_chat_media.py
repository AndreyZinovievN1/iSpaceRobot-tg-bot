from __future__ import annotations

import json
from datetime import datetime, timezone
from typing import Any, Iterable

from app.ai_chat.models import (
    MediaAsset,
    MediaKind,
    MediaSafetySource,
    MediaSafetyStatus,
)
from app.crud_tables.table_ai_chat_helpers import parse_execute_count, row_get


MEDIA_CATALOG_LIMIT_PER_CHAT = 1000


def normalize_metadata(value: Any) -> dict[str, Any]:
    pass  # TODO: Commercial logic


def media_asset_from_row(row: Any) -> MediaAsset:
    pass  # TODO: Commercial logic


class AIChatMediaTable:
    def __init__(self, db):
        pass  # TODO: Commercial logic

    async def upsert_media_asset(self, asset: MediaAsset) -> None:
        pass  # TODO: Commercial logic

    async def fetch_media_asset_by_unique(
        self,
        *,
        chat_id: int,
        file_unique_id: str,
        kind: MediaKind,
    ) -> MediaAsset | None:
        pass  # TODO: Commercial logic

    async def fetch_media_asset_by_id(self, asset_id: int) -> MediaAsset | None:
        pass  # TODO: Commercial logic

    async def delete_media_asset_by_id(self, asset_id: int) -> int:
        pass  # TODO: Commercial logic

    async def fetch_approved_media_asset(
        self,
        *,
        chat_id: int,
        kinds: Iterable[MediaKind],
        exclude_file_ids: Iterable[str] = (),
        reuse_cooldown_seconds: int = 3600,
        fresh_delay_seconds: int = 0,
        exclude_safety_reasons: Iterable[str] = (),
    ) -> MediaAsset | None:
        pass  # TODO: Commercial logic

    async def count_approved_media_assets(
        self,
        *,
        chat_id: int,
        kinds: Iterable[MediaKind],
        fresh_delay_seconds: int = 0,
        exclude_safety_reasons: Iterable[str] = (),
    ) -> int:
        pass  # TODO: Commercial logic

    async def mark_media_used(
        self,
        *,
        chat_id: int,
        file_id: str,
    ) -> None:
        pass  # TODO: Commercial logic

    async def record_media_send_failure(
        self,
        *,
        chat_id: int,
        file_id: str,
        error_text: str,
    ) -> int:
        pass  # TODO: Commercial logic

    async def clear_media_send_failures(
        self,
        *,
        chat_id: int,
        file_id: str,
    ) -> None:
        pass  # TODO: Commercial logic

    async def cleanup_media_catalog_limit(
        self,
        *,
        chat_id: int,
        limit: int = MEDIA_CATALOG_LIMIT_PER_CHAT,
    ) -> int:
        pass  # TODO: Commercial logic
