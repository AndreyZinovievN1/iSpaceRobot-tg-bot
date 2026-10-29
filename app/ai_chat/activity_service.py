import random
from datetime import datetime, timezone

from app.ai_chat.space_generator import generate_space_phrase
from app.ai_chat.space_mood import detect_mood
from app.ai_chat.filters import is_safe_phrase
from app.ai_chat.repository import AIChatRepository
from app.ai_chat.style import apply_space_style


async def get_recent_messages(
    db,
    chat_id: int,
    limit: int = 40,
) -> list[str]:
    pass  # TODO: Commercial logic


async def save_idle_message(
    db,
    chat_id: int,
    phrase: str,
    *,
    sent_message=None,
) -> None:
    pass  # TODO: Commercial logic


async def update_last_action(db, chat_id: int) -> None:
    pass  # TODO: Commercial logic


async def space_idle_tick(bot, db) -> None:
    """
    Запускается планировщиком из main.py.

    Space может сам написать только в чат, где:
    1. Agent включён.
    2. Недавно была активность.
    3. Он давно ничего не отправлял.
    4. В чате сейчас не идёт спор.
    """
    pass  # TODO: Commercial logic
