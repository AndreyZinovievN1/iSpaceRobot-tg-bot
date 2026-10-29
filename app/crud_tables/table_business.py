from config import logger
from app.db import db


async def save_business_message(msg_id: int, conn_id: str, user_id: int, chat_id: int, text: str):
    """
    Старая совместимая версия.
    Ничего лишнего в БД не требует.
    Нужна, чтобы удалённые текстовые сообщения снова работали как раньше.
    """
    pass  # TODO: Commercial logic


async def mark_message_deleted(msg_ids: list, conn_id: str):
    pass  # TODO: Commercial logic


async def update_business_message(msg_id: int, conn_id: str, new_text: str):
    pass  # TODO: Commercial logic


async def get_chat_history(chat_id: int, limit: int = 10, offset: int = 0):
    pass  # TODO: Commercial logic


async def get_chat_history_paged(chat_id: int, limit: int = 10, offset: int = 0):
    pass  # TODO: Commercial logic


async def get_business_clients(chat_id: int, limit: int = 10, offset: int = 0):
    pass  # TODO: Commercial logic


async def get_message_by_id(msg_id: int, conn_id: str):
    """
    Возвращает dict, чтобы работали old_data['content'] и old_data.get(...).
    Добавлен fallback по message_id на случай, если Telegram вернул другой connection_id.
    """
    pass  # TODO: Commercial logic
