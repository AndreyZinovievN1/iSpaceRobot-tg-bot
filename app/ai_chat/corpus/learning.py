from __future__ import annotations

import re
from collections import Counter
from typing import Any

from app.ai_chat.models import LearningDecision, LearningSkipReason


MAX_LEARNING_TEXT_LENGTH = 500
MAX_WORDS_PER_MESSAGE = 16

LINK_RE = re.compile(
    r"(https?://|www\.|t\.me/|telegram\.me/|tg://)",
    re.IGNORECASE,
)
MENTION_RE = re.compile(r"(^|\s)@[a-zA-Z0-9_]{3,32}\b")
BOT_TOKEN_RE = re.compile(r"\b\d{6,12}:[A-Za-z0-9_-]{30,}\b")
API_SECRET_RE = re.compile(
    r"\b(?:sk-[A-Za-z0-9_-]{20,}|"
    r"(?:api[_-]?key|token|secret|password|passwd|пароль|токен|секрет)"
    r"\s*[:=]\s*\S+)",
    re.IGNORECASE,
)
CONNECTION_SECRET_RE = re.compile(
    r"\b(?:postgres(?:ql)?|mysql|mongodb|redis)://",
    re.IGNORECASE,
)
TEXT_SYMBOL_RE = re.compile(r"[A-Za-zА-Яа-яЁё0-9]")
WORD_RE = re.compile(r"[A-Za-zА-Яа-яЁё0-9_]{3,32}")


def get_message_text(message: Any) -> str:
    pass  # TODO: Commercial logic


def has_supported_media(message: Any) -> bool:
    pass  # TODO: Commercial logic


def build_user_name(user: Any) -> str:
    pass  # TODO: Commercial logic


def normalize_learning_text(text: str | None) -> str | None:
    pass  # TODO: Commercial logic


def extract_words(text: str, *, limit: int = MAX_WORDS_PER_MESSAGE) -> tuple[str, ...]:
    pass  # TODO: Commercial logic


def check_learning_text(text: str | None) -> LearningDecision:
    pass  # TODO: Commercial logic
