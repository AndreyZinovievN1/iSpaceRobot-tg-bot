from config import logger
from ..db import db


async def add_user_name_history(user_id: int, username: str | None, full_name: str):
    """
    Сохраняет историю имён пользователя.
    """
    pass  # TODO: Commercial logic


async def get_user_name_history(user_id: int, limit: int = 3):
    """
    Возвращает последние варианты имён пользователя.
    """
    pass  # TODO: Commercial logic


async def add_user_seen_chat(user_id: int, chat_id: int, chat_title: str):
    """
    Сохраняет чат, где бот видел пользователя.
    И увеличивает счётчик сообщений в этом чате.
    """
    pass  # TODO: Commercial logic


async def get_user_seen_chats(user_id: int, limit: int = 3):
    """
    Возвращает последние чаты, где бот видел пользователя.
    """
    pass  # TODO: Commercial logic
