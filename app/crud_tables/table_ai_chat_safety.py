from __future__ import annotations

from app.ai_chat.models import (
    MediaAsset,
    MediaSafetySource,
    MediaSafetyStatus,
)
from app.crud_tables.table_ai_chat_helpers import parse_execute_count
from app.crud_tables.table_ai_chat_media import media_asset_from_row


class AIChatSafetyTable:
    def __init__(self, db):
        pass  # TODO: Commercial logic

    async def set_media_safety_status(
        self,
        *,
        chat_id: int,
        file_id: str | None = None,
        file_unique_id: str | None = None,
        safety_status: MediaSafetyStatus,
        reason: str = "manual",
        source: MediaSafetySource = MediaSafetySource.MANUAL,
        decided_by_user_id: int | None = None,
    ) -> int:
        pass  # TODO: Commercial logic

    async def set_media_safety_status_by_asset_id(
        self,
        *,
        asset_id: int,
        safety_status: MediaSafetyStatus,
        reason: str,
        source: MediaSafetySource = MediaSafetySource.MANUAL,
        decided_by_user_id: int | None = None,
    ) -> int:
        pass  # TODO: Commercial logic

    async def upsert_media_safety_rule(
        self,
        *,
        chat_id: int,
        rule_type: str,
        file_id: str | None = None,
        file_unique_id: str | None = None,
        reason: str,
        source: MediaSafetySource = MediaSafetySource.MANUAL,
        decided_by_user_id: int | None = None,
    ) -> None:
        pass  # TODO: Commercial logic

    async def fetch_media_safety_rule(
        self,
        *,
        chat_id: int,
        rule_type: str,
        file_id: str | None = None,
        file_unique_id: str | None = None,
    ):
        pass  # TODO: Commercial logic

    async def deactivate_media_safety_rules(
        self,
        *,
        chat_id: int,
        file_id: str | None = None,
        file_unique_id: str | None = None,
    ) -> int:
        pass  # TODO: Commercial logic

    async def log_media_safety_event(
        self,
        *,
        chat_id: int,
        file_id: str | None,
        file_unique_id: str | None,
        safety_status: MediaSafetyStatus,
        reason: str,
        source: MediaSafetySource,
        decided_by_user_id: int | None = None,
    ) -> None:
        pass  # TODO: Commercial logic

    async def list_media_assets_by_status(
        self,
        *,
        chat_id: int,
        safety_status: MediaSafetyStatus,
        limit: int = 50,
    ) -> list[MediaAsset]:
        pass  # TODO: Commercial logic

    async def mark_media_broken(
        self,
        *,
        chat_id: int,
        file_id: str,
        file_unique_id: str | None = None,
        reason: str = "broken_send_failed",
    ) -> int:
        pass  # TODO: Commercial logic
