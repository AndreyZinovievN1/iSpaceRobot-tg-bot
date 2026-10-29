from __future__ import annotations

import asyncio
import logging
import time

from app.crud_tables.table_ai_chat_helpers import row_get


logger = logging.getLogger(__name__)

RETRIEVAL_SHADOW_LIMIT = 10
RETRIEVAL_SHADOW_TIMEOUT_SECONDS = 0.250


def _log_shadow_metric(
    *,
    chat_id: int,
    message_thread_id: int | None,
    rows,
    duration_ms: float,
) -> None:
    pass  # TODO: Commercial logic


async def run_retrieval_shadow(
    repo,
    *,
    chat_id: int,
    source_text: str | None,
    message_thread_id: int | None = None,
    exclude_response_message_id: int | None = None,
):
    pass  # TODO: Commercial logic
