from config import logger
from app.db import db

async def add_admin(chat_id: int, can_broadcast: bool=False):
    pass  # TODO: Commercial logic

async def get_admin_by_chat(chat_id: int):
    pass  # TODO: Commercial logic

async def remove_admin(chat_id: int):
    pass  # TODO: Commercial logic

async def update_admin_broadcast_flag(chat_id: int, can_broadcast: bool):
    pass  # TODO: Commercial logic
