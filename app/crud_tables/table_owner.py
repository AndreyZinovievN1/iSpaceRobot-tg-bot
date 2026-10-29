from config import logger
from app.db import db

async def check_is_owner(chat_id: int):
    pass  # TODO: Commercial logic

async def update_owner(new_chat_id: int):
    pass  # TODO: Commercial logic

async def update_gallery(chat_id: int, new_gallery: list[int]):
    pass  # TODO: Commercial logic
    
async def delete_gallery():
    pass  # TODO: Commercial logic
    
async def get_gallery() -> list[int]:
    pass  # TODO: Commercial logic
    
async def get_admin_mode():
    pass  # TODO: Commercial logic

async def set_admin_mode(enabled: bool):
    pass  # TODO: Commercial logic
