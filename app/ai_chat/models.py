from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import StrEnum
from typing import Any


class MessageRole(StrEnum):
    USER = "user"
    SPACE = "space"


class ActionType(StrEnum):
    NOTHING = "nothing"
    TEXT = "text"
    REACTION = "reaction"
    MEME = "meme"
    VOICE = "voice"
    STICKER = "sticker"
    GIF = "gif"
    EMOJI = "emoji"


class ChatDevelopmentStage(StrEnum):
    SEED = "seed"
    WARMING = "warming"
    ACTIVE = "active"
    MATURE = "mature"


class MediaKind(StrEnum):
    PHOTO = "photo"
    VIDEO = "video"
    ANIMATION = "animation"
    DOCUMENT_ANIMATION = "document_animation"
    STICKER = "sticker"
    CUSTOM_EMOJI = "custom_emoji"
    UNKNOWN = "unknown"


class MediaSafetyStatus(StrEnum):
    PENDING = "pending"
    APPROVED = "approved"
    BLOCKED = "blocked"


class MediaSafetySource(StrEnum):
    DEFAULT = "default"
    ALLOWLIST = "allowlist"
    DENYLIST = "denylist"
    MANUAL = "manual"
    PROVIDER = "provider"


class LearningEventType(StrEnum):
    SAVED = "saved"
    SKIPPED = "skipped"
    CLEANUP = "cleanup"


class LearningSkipReason(StrEnum):
    DISABLED = "disabled"
    UNSUPPORTED_CHAT = "unsupported_chat"
    EMPTY_TEXT = "empty_text"
    BOT_AUTHOR = "bot_author"
    COMMAND = "command"
    LINK = "link"
    MENTION = "mention"
    SECRET = "secret"
    TOO_SHORT = "too_short"
    TOO_LONG = "too_long"
    NO_TEXT_SYMBOLS = "no_text_symbols"
    REPEATED_CHARS = "repeated_chars"
    REPEATED_WORDS = "repeated_words"


@dataclass(frozen=True, slots=True)
class ChatMessageRecord:
    chat_id: int
    user_id: int
    user_name: str
    text: str
    role: MessageRole = MessageRole.USER


@dataclass(frozen=True, slots=True)
class LearningDecision:
    accepted: bool
    reason: str
    text: str | None = None
    words: tuple[str, ...] = ()


@dataclass(frozen=True, slots=True)
class LearningResult:
    saved: bool
    reason: str
    chat_id: int | None = None
    user_id: int | None = None
    text: str | None = None
    message_id: int | None = None
    words_count: int = 0
    cleanup_deleted: int = 0


@dataclass(frozen=True, slots=True)
class DecisionResult:
    action: ActionType
    reason: str
    mood_name: str
    stage: ChatDevelopmentStage
    confidence: float = 0.0
    reply_to_message: bool = True
    cooldown_left: float = 0.0
    quota_left: int | None = None

    @property
    def should_reply(self) -> bool:
        return self.action != ActionType.NOTHING


@dataclass(frozen=True, slots=True)
class ChatMemory:
    chat_id: int
    accepted_messages: int = 0
    skipped_messages: int = 0
    last_user_message_at: datetime | None = None
    last_learned_message_at: datetime | None = None
    last_save_reason: str | None = None
    last_skip_reason: str | None = None
    updated_at: datetime | None = None


@dataclass(frozen=True, slots=True)
class UserMemory:
    chat_id: int
    user_id: int
    user_name: str | None = None
    accepted_messages: int = 0
    skipped_messages: int = 0
    last_message_text: str | None = None
    last_message_at: datetime | None = None
    updated_at: datetime | None = None


@dataclass(frozen=True, slots=True)
class MediaAsset:
    chat_id: int
    file_id: str
    file_unique_id: str | None = None
    kind: MediaKind = MediaKind.UNKNOWN
    safety_status: MediaSafetyStatus = MediaSafetyStatus.PENDING
    emoji: str | None = None
    set_name: str | None = None
    context: str | None = None
    usage_count: int = 0
    last_used_at: datetime | None = None
    safety_reason: str | None = None
    safety_source: MediaSafetySource = MediaSafetySource.DEFAULT
    safety_decided_by_user_id: int | None = None
    safety_decided_at: datetime | None = None
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True, slots=True)
class MediaSafetyDecision:
    status: MediaSafetyStatus
    reason: str
    source: MediaSafetySource = MediaSafetySource.DEFAULT
    decided_by_user_id: int | None = None
    confidence: float | None = None
