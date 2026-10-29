from __future__ import annotations

import asyncio
import logging
import os
import time
from dataclasses import dataclass

from app.crud_tables.table_ai_chat_helpers import row_get


logger = logging.getLogger(__name__)

LOCAL_RETRIEVAL_ENABLED_ENV = "SPACE_LOCAL_RETRIEVAL_ENABLED"
LOCAL_RETRIEVAL_LIMIT = 10
LOCAL_RETRIEVAL_MIN_SIMILARITY = 0.92
LOCAL_RETRIEVAL_TIMEOUT_SECONDS = 0.250


@dataclass(frozen=True)
class LocalRetrievalResult:
    candidate: object | None = None
    pair_count_returned: int = 0
    eligible_count: int = 0
    best_similarity: float = 0.0
    best_pair_id: int | None = None
    reason: str = "not_found"
    duration_ms: float = 0.0


def is_local_retrieval_enabled() -> bool:
    pass  # TODO: Commercial logic


def log_local_retrieval(
    *,
    chat_id: int,
    result: LocalRetrievalResult,
    used: bool,
    reason: str | None = None,
) -> None:
    pass  # TODO: Commercial logic


async def run_local_retrieval(
    repo,
    *,
    chat_id: int,
    source_text: str | None,
    message_thread_id: int | None = None,
    exclude_response_message_id: int | None = None,
) -> LocalRetrievalResult:
    pass  # TODO: Commercial logic
