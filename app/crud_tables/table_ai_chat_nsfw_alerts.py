from __future__ import annotations

from typing import Any

from app.crud_tables.table_ai_chat_helpers import row_get


class AIChatNSFWAlertsTable:
    def __init__(self, db):
        pass  # TODO: Commercial logic

    async def claim_alert(
        self,
        *,
        asset_id: int,
        chat_id: int,
        verdict: str,
    ):
        pass  # TODO: Commercial logic

    async def fetch_alert_payload(self, *, asset_id: int):
        pass  # TODO: Commercial logic

    async def mark_media_sent(
        self,
        *,
        alert_id: int,
        media_message_id: int,
    ) -> None:
        pass  # TODO: Commercial logic

    async def mark_alert_sent(
        self,
        *,
        alert_id: int,
        media_message_id: int,
        metadata_message_id: int,
    ) -> None:
        pass  # TODO: Commercial logic

    async def mark_alert_error(
        self,
        *,
        alert_id: int,
        error_stage: str,
        error_type: str,
    ) -> None:
        pass  # TODO: Commercial logic

    async def fetch_alert_by_id(self, alert_id: int):
        pass  # TODO: Commercial logic

    async def claim_action(
        self,
        *,
        alert_id: int,
        action: str,
        acted_by_user_id: int,
    ) -> tuple[Any, bool]:
        pass  # TODO: Commercial logic

    async def complete_action(
        self,
        *,
        alert_id: int,
        action: str,
        acted_by_user_id: int,
    ) -> None:
        pass  # TODO: Commercial logic

    async def release_action(
        self,
        *,
        alert_id: int,
        action: str,
        acted_by_user_id: int,
    ) -> None:
        pass  # TODO: Commercial logic
