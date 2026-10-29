from __future__ import annotations

from app.crud_tables.table_ai_chat_helpers import parse_execute_count, row_get


class AIChatMaintenanceTable:
    def __init__(self, db):
        pass  # TODO: Commercial logic

    async def _dry_count(self, query: str, *args) -> int:
        pass  # TODO: Commercial logic

    async def _delete_count(self, query: str, *args) -> int:
        pass  # TODO: Commercial logic

    async def fetch_maintenance_chat_ids(self) -> list[int]:
        pass  # TODO: Commercial logic

    async def count_old_messages(
        self,
        chat_id: int,
        *,
        retention_days: int,
        batch_size: int,
    ) -> int:
        pass  # TODO: Commercial logic

    async def count_excess_messages(
        self,
        chat_id: int,
        *,
        max_messages: int,
        batch_size: int,
    ) -> int:
        pass  # TODO: Commercial logic

    async def delete_old_messages(
        self,
        chat_id: int,
        *,
        retention_days: int,
        max_messages: int,
        batch_size: int,
    ) -> int:
        pass  # TODO: Commercial logic

    async def count_old_learning_events(
        self,
        chat_id: int,
        *,
        retention_days: int,
        batch_size: int,
    ) -> int:
        pass  # TODO: Commercial logic

    async def delete_old_learning_events(
        self,
        chat_id: int,
        *,
        retention_days: int,
        batch_size: int,
    ) -> int:
        pass  # TODO: Commercial logic

    async def count_stale_memory(
        self,
        chat_id: int,
        *,
        retention_days: int,
        batch_size: int,
    ) -> dict[str, int]:
        pass  # TODO: Commercial logic

    async def delete_stale_memory(
        self,
        chat_id: int,
        *,
        retention_days: int,
        batch_size: int,
    ) -> dict[str, int]:
        pass  # TODO: Commercial logic

    async def count_old_media_assets(
        self,
        chat_id: int,
        *,
        pending_days: int,
        blocked_days: int,
        delete_approved: bool,
        batch_size: int,
        approved_days: int,
    ) -> int:
        pass  # TODO: Commercial logic

    async def delete_old_media_assets(
        self,
        chat_id: int,
        *,
        pending_days: int,
        blocked_days: int,
        delete_approved: bool,
        batch_size: int,
        approved_days: int,
    ) -> int:
        pass  # TODO: Commercial logic
