from __future__ import annotations

import asyncio
import logging
import socket
import uuid
from dataclasses import dataclass, field, replace
from typing import Any, Awaitable, Callable

from app.ai_chat.models import MediaAsset
from app.ai_chat.nsfw_alert_service import NSFWAlertService
from app.ai_chat.nsfw_frame_extractor import (
    ExtractedNSFWFrame,
    NSFWFrameDecodeError,
    NSFWFrameExtractionError,
    NSFWFrameExtractionResult,
    NSFWFrameExtractionTimeout,
    NSFWMediaTooLargeError,
    NSFWUnsupportedMediaError,
    extract_frames_for_asset,
)
from app.ai_chat.nsfw_provider import (
    NSFWProviderError,
    NSFWProviderUnavailableError,
    VitMiniExplicitContentProvider,
    get_nsfw_provider,
)
from app.ai_chat.nsfw_provider_config import NSFWProviderThresholds, verdict_from_scores
from app.ai_chat.nsfw_config import load_nsfw_cascade_config, nsfw_cascade_enabled
from app.ai_chat.nsfw_cascade_service import is_hentai_borderline_candidate
from app.ai_chat.nsfw_types import NSFWFrameResult, NSFWScanResult, NSFWVerdict
from app.ai_chat.repository import AIChatRepository, row_get


logger = logging.getLogger(__name__)

Extractor = Callable[[Any, MediaAsset], Awaitable[NSFWFrameExtractionResult]]


@dataclass(frozen=True, slots=True)
class NSFWJobProcessResult:
    job_id: int
    asset_id: int | None
    success: bool
    reason: str


@dataclass(frozen=True, slots=True)
class NSFWWorkerRunResult:
    claimed: int = 0
    processed: int = 0
    succeeded: int = 0
    failed: int = 0
    skipped: int = 0
    results: tuple[NSFWJobProcessResult, ...] = field(default_factory=tuple)


def _default_worker_id() -> str:
    pass  # TODO: Commercial logic


def _score(result: NSFWScanResult, key: str) -> float:
    pass  # TODO: Commercial logic


def _compact_failure_reason(reason: str) -> str:
    pass  # TODO: Commercial logic


def _fail_closed_asset_status(asset: MediaAsset) -> str:
    pass  # TODO: Commercial logic


PARTIAL_FRAMES_REASON = "nsfw_scan_partial_frames"


def apply_partial_extraction_guard(
    result: NSFWScanResult,
    *,
    extraction_complete: bool,
) -> NSFWScanResult:
    """Fail closed when media was scanned on partial frame evidence.

    A video whose sampled positions could not all be decoded may hide explicit
    content inside the frames that never made it through the decoder. Such a
    scan must never be auto-approved silently, so a SAFE verdict is downgraded
    to UNCERTAIN, which routes the asset to the cascade re-check and/or the
    owner alert. Non-SAFE verdicts are returned untouched.
    """
    pass  # TODO: Commercial logic


def aggregate_frame_scan_results(
    frame_results: list[tuple[ExtractedNSFWFrame, NSFWScanResult]],
    *,
    thresholds: NSFWProviderThresholds,
    provider_name: str,
    model_name: str,
    model_version: str | None = None,
) -> NSFWScanResult:
    pass  # TODO: Commercial logic


class NSFWScanWorker:
    def __init__(
        self,
        bot,
        db,
        *,
        repo_factory: Callable[[Any], AIChatRepository] = AIChatRepository,
        provider: VitMiniExplicitContentProvider | None = None,
        extractor: Extractor | None = None,
        worker_id: str | None = None,
        lock_seconds: int = 300,
        retry_delay_seconds: int = 300,
        alert_service: Any | None = None,
        cascade_service: Any | None = None,
    ) -> None:
        pass  # TODO: Commercial logic

    async def run_once(self, *, limit: int = 5) -> NSFWWorkerRunResult:
        pass  # TODO: Commercial logic

    async def _process_terminal_recovery(self, job: Any) -> NSFWJobProcessResult:
        pass  # TODO: Commercial logic

    async def _handle_unexpected_job_exception(
        self,
        job: Any,
        exc: Exception,
    ) -> NSFWJobProcessResult:
        pass  # TODO: Commercial logic

    async def _process_job(self, job: Any) -> NSFWJobProcessResult:
        pass  # TODO: Commercial logic

    async def _scan_extracted_frames(self, extraction: NSFWFrameExtractionResult) -> NSFWScanResult:
        pass  # TODO: Commercial logic

    async def _send_alert_fail_open(
        self,
        *,
        asset: MediaAsset,
        asset_id: int,
        job_id: int,
        result: NSFWScanResult,
    ) -> bool:
        pass  # TODO: Commercial logic

    async def _handle_terminal_failure(
        self,
        *,
        asset: MediaAsset,
        asset_id: int,
        job_id: int,
        reason: str,
        provider: str,
    ) -> None:
        pass  # TODO: Commercial logic

    async def _fail_job(self, job: Any, exc: Exception, *, reason: str) -> bool:
        pass  # TODO: Commercial logic


async def run_once(
    bot,
    db,
    *,
    limit: int = 5,
    provider: VitMiniExplicitContentProvider | None = None,
    extractor: Extractor | None = None,
    repo_factory: Callable[[Any], AIChatRepository] = AIChatRepository,
    worker_id: str | None = None,
) -> NSFWWorkerRunResult:
    pass  # TODO: Commercial logic
