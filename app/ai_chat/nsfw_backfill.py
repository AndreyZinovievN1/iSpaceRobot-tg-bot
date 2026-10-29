from __future__ import annotations

import asyncio
import logging
from dataclasses import dataclass

from app.ai_chat.repository import AIChatRepository


logger = logging.getLogger(__name__)

BACKFILL_BATCH_SIZE = 500


@dataclass(frozen=True, slots=True)
class NSFWBackfillResult:
    assets_seen: int = 0
    jobs_created: int = 0
    skipped: int = 0


def _batch_size(value: int = BACKFILL_BATCH_SIZE) -> int:
    pass  # TODO: Commercial logic


async def backfill_pending_nsfw_scan_jobs(
    db,
    *,
    batch_size: int = BACKFILL_BATCH_SIZE,
    repo_factory=AIChatRepository,
) -> NSFWBackfillResult:
    pass  # TODO: Commercial logic


async def main() -> None:
    pass  # TODO: Commercial logic


if __name__ == "__main__":
    asyncio.run(main())
