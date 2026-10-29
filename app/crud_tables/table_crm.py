from config import logger
from app.db import db

async def upsert_client(user_id: int, username: str, full_name: str):
    pass  # TODO: Commercial logic

async def get_client_info(user_id: int):
    pass  # TODO: Commercial logic

async def get_all_clients(owner_id: int, limit: int = 20, offset: int = 0):
    pass  # TODO: Commercial logic

async def update_client_status(user_id: int, new_status: str):
    pass  # TODO: Commercial logic

async def update_client_notes(user_id: int, notes: str):
    pass  # TODO: Commercial logic

async def get_crm_stats(user_id: int):
    pass  # TODO: Commercial logic

async def get_all_client_ids():
    pass  # TODO: Commercial logic
