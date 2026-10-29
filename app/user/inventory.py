from aiogram import types, Router, F
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton

from app.crud_tables.table_users import get_user_by_chat_id
from app.crud_tables.table_inventory import get_user_inventory
from app.crud_tables.table_users import (
    update_user_active_title, update_user_active_emoji,
    update_user_active_reply, update_user_active_greeting,
    update_user_active_button, update_user_active_chart
)

router = Router()

async def get_inventory_data(user_id: int, first_name: str):
    pass  # TODO: Commercial logic

@router.message(Command("inv"))
async def show_inventory(message: types.Message):
    pass  # TODO: Commercial logic

@router.callback_query(F.data.startswith("inv_equip_"))
async def handle_inventory_equip(callback: types.CallbackQuery):
    pass  # TODO: Commercial logic
