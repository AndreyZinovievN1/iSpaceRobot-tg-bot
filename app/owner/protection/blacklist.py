from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters.command import Command

from app.variables_and_funcs import is_owner
from app.kbs import when_users_blacklist_ikb
from app.crud_tables.table_users import get_user_by_chat_id
from app.db import db

router = Router()

@router.message(Command("чс", prefix="!"))
async def show_blacklist_cmd(message: Message):
    pass  # TODO: Commercial logic

@router.callback_query(F.data == "users_blacklist")
async def cb_users_blacklist(query: CallbackQuery):
    # Логика обновления меню ЧС пользователей
    pass

@router.callback_query(F.data == "groups_blacklist")
async def cb_groups_blacklist(query: CallbackQuery):
    # Логика обновления меню ЧС групп
    pass
