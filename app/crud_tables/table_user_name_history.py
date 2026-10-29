from config import logger
from app.db import db


async def get_last_name(user_id: int):
    """
    Получить последний сохранённый ник пользователя
    """
    pass  # TODO: Commercial logic


async def add_name_history(user_id: int, name: str):
    """
    Добавить запись смены ника
    """
    pass  # TODO: Commercial logic


async def save_name_if_changed(user_id: int, name: str):
    """
    Сохраняет ник только если он изменился
    """
    pass  # TODO: Commercial logic


async def get_name_history(user_id: int, limit: int = 20):
    """
    Получить историю ников пользователя
    """
    pass  # TODO: Commercial logic
