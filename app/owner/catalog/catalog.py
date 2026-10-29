from aiogram import Router
from aiogram.types import Message
from app.filters.catalog_filter import IsCatalogManager
from app.crud_tables.table_catalog_gifs import (
    get_gif_from_catalog_by_gif_id, add_gif_to_catalog, update_message_id_for_gif
)
from config import bot

router = Router()

@router.message(IsCatalogManager())
async def handle_new_catalog_gif(message: Message, catalog_type: str):
    # Если фильтр пропустил, значит сообщение удаляем сразу
    pass  # TODO: Commercial logic
