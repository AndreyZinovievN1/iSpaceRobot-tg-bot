from aiogram import Router
from aiogram.types import Message

from config import bot
from app.variables_and_funcs import is_owner
from app.crud_tables.table_private_catalog_gifs import (
    get_gif_from_private_catalog_by_gif_id,
    add_gif_to_private_catalog,
    update_message_id_for_private_gif,
)

# ВАЖНО: этот роутер должен висеть ТОЛЬКО на твоём приватном чате/канале
# Самый простой способ — отдельный фильтр по chat_id (см. шаг 4)
router = Router()

@router.message()
async def handle_new_private_catalog_gif(message: Message):
    # 1) Только ты
    pass  # TODO: Commercial logic
