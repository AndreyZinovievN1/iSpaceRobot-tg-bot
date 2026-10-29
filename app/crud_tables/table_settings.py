from config import logger
from app.db import db

async def get_settings_by_group_id(group_id: int):
    pass  # TODO: Commercial logic

async def add_settings(group_id: int):
    pass  # TODO: Commercial logic

async def update_settings(column_name: str, value, group_id: int):
    pass  # TODO: Commercial logic
    
async def update_msg_count_for_group(group_id: int, count: int = None):
    pass  # TODO: Commercial logic

async def update_welcome_text(welcome_text: str, group_id: int):
    pass  # TODO: Commercial logic

async def update_members_count(members_count: int, group_id: int):
    pass  # TODO: Commercial logic

async def remove_settings(group_id: int):
    pass  # TODO: Commercial logic
        
LANG_ALLOWED = {"ru", "en", "ua"}

async def update_chat_lang(group_id: int, lang: str | None = None) -> tuple[str, bool]:
    pass  # TODO: Commercial logic

async def get_total_messages_in_groups():
    pass  # TODO: Commercial logic
