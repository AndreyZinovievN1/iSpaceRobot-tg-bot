import re
from difflib import SequenceMatcher


BAD_PATTERNS = [
    r"https?://",
    r"t\.me/",
    r"@\w+",
    r"^\s*[\/!\.\+\-]",
    r"\b(?:free|bonus|airdrop|crypto|casino)\b",
]

BLOCKED_WORDS = {
    "нацизм",
    "суицид",
}


def normalize_phrase(text: str | None) -> str | None:
    pass  # TODO: Commercial logic


def is_safe_phrase(text: str | None, recent_messages: list[str] | None = None) -> bool:
    pass  # TODO: Commercial logic


def choose_safe_phrase(phrases: list[str], recent_messages: list[str]) -> str | None:
    pass  # TODO: Commercial logic
