import logging
import random
import re

from app.ai_chat.decision_policy import is_novel_phrase, normalize_for_novelty
from app.ai_chat.markov_cache import get_markov_cache
from app.ai_chat.repository import AIChatRepository, row_get


BAD_PATTERNS = [
    r"https?://",
    r"t\.me/",
    r"@\w+",
    r"^\s*[\/!\.\+\-]",
]

logger = logging.getLogger(__name__)


def clean_phrase(text: str | None) -> str | None:
    pass  # TODO: Commercial logic


async def get_training_texts(db, chat_id: int, limit: int = 2200) -> list[str]:
    pass  # TODO: Commercial logic


def phrase_words(text: str | None) -> set[str]:
    pass  # TODO: Commercial logic


def score_phrase(
    phrase: str,
    recent_messages: list[str],
    *,
    memory_keywords: list[str] | None = None,
    source_text: str | None = None,
) -> int:
    pass  # TODO: Commercial logic


async def generate_space_phrase(
    db,
    chat_id: int,
    recent_messages: list[str],
    variants_count: int = 35,
    *,
    settings=None,
    messages_count: int | None = None,
    chat_memory=None,
    user_memory=None,
    memory_keywords: list[str] | None = None,
    source_text: str | None = None,
) -> str | None:
    pass  # TODO: Commercial logic
