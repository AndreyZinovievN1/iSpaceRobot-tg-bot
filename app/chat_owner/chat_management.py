from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext

from app.variables_and_funcs import (
    is_owner, is_chat_creator, is_chat_admin, delete_after_delay
)
from app.crud_tables.table_settings import get_settings_by_group_id
from config import bot
from app.kbs import chat_management_ikb
from app.lang import tr_msg

router = Router()

@router.callback_query(F.data == "chat_management_menu")
async def settings(query: CallbackQuery, state: FSMContext):
    pass  # TODO: Commercial logic


@router.message(Command("админ", prefix="+"))
async def force_marriage(message: Message):
    pass  # TODO: Commercial logic


@router.message(Command("админ", prefix="-"))
async def force_marriage(message: Message):
    pass  # TODO: Commercial logic
