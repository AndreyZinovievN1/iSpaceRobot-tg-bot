from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum
from typing import Any

from app.ai_chat.models import MediaKind, MediaSafetyStatus


class NSFWScanStatus(StrEnum):
    PENDING = "pending"
    QUEUED = "queued"
    PROCESSING = "processing"
    DONE = "done"
    FAILED = "failed"
    UNSUPPORTED = "unsupported"
    TOO_LARGE = "too_large"


class NSFWMediaType(StrEnum):
    PHOTO = "photo"
    VIDEO = "video"
    ANIMATION = "animation"
    DOCUMENT_ANIMATION = "document_animation"
    STICKER = "sticker"
    CUSTOM_EMOJI = "custom_emoji"
    UNKNOWN = "unknown"

    @classmethod
    def from_media_kind(cls, kind: MediaKind | str | None) -> "NSFWMediaType":
        if kind is None:
            return cls.UNKNOWN

        value = kind.value if isinstance(kind, MediaKind) else str(kind)
        try:
            return cls(value)
        except ValueError:
            return cls.UNKNOWN


class NSFWVerdict(StrEnum):
    SAFE = "safe"
    BLOCKED = "blocked"
    UNCERTAIN = "uncertain"
    FAILED = "failed"
    UNSUPPORTED = "unsupported"
    TOO_LARGE = "too_large"

    @property
    def safety_status(self) -> MediaSafetyStatus:
        if self == NSFWVerdict.SAFE:
            return MediaSafetyStatus.APPROVED
        if self == NSFWVerdict.BLOCKED:
            return MediaSafetyStatus.BLOCKED
        return MediaSafetyStatus.PENDING


@dataclass(frozen=True, slots=True)
class NSFWFrameResult:
    frame_index: int
    scores: dict[str, float] = field(default_factory=dict)
    verdict: NSFWVerdict = NSFWVerdict.UNCERTAIN
    reason: str | None = None


@dataclass(frozen=True, slots=True)
class NSFWScanResult:
    verdict: NSFWVerdict
    safety_status: MediaSafetyStatus
    reason: str
    provider: str
    model_name: str
    model_version: str | None = None
    scores: dict[str, Any] = field(default_factory=dict)
    frame_results: tuple[NSFWFrameResult, ...] = ()
    frames_checked: int = 0
    max_pornography_score: float | None = None
    max_hentai_score: float | None = None
    max_sensual_score: float | None = None
    content_hash: str | None = None
    phash: str | None = None
    error: str | None = None

    @classmethod
    def from_verdict(
        cls,
        *,
        verdict: NSFWVerdict,
        reason: str,
        provider: str,
        model_name: str,
        model_version: str | None = None,
        scores: dict[str, Any] | None = None,
        frame_results: tuple[NSFWFrameResult, ...] = (),
        frames_checked: int = 0,
        max_pornography_score: float | None = None,
        max_hentai_score: float | None = None,
        max_sensual_score: float | None = None,
        content_hash: str | None = None,
        phash: str | None = None,
        error: str | None = None,
    ) -> "NSFWScanResult":
        return cls(
            verdict=verdict,
            safety_status=verdict.safety_status,
            reason=reason,
            provider=provider,
            model_name=model_name,
            model_version=model_version,
            scores=scores or {},
            frame_results=frame_results,
            frames_checked=frames_checked,
            max_pornography_score=max_pornography_score,
            max_hentai_score=max_hentai_score,
            max_sensual_score=max_sensual_score,
            content_hash=content_hash,
            phash=phash,
            error=error,
        )
