from config import logger
from app.db import db

async def add_gif_to_catalog(gif_id: str, catalog_type: str = "public") -> int | None:
    pass  # TODO: Commercial logic

async def update_message_id_for_gif(gif_db_id: int, message_id: int):
    pass  # TODO: Commercial logic

async def get_gif_from_catalog_by_id(id: int):
    pass  # TODO: Commercial logic

async def get_gif_from_catalog_by_gif_id(gif_id: str):
    pass  # TODO: Commercial logic

async def delete_gif_from_catalog(gif_id: str):
    pass  # TODO: Commercial logic
