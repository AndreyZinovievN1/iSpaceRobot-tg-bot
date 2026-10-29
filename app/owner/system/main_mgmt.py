from aiogram import Router
from aiogram.types import Message
from aiogram.filters.command import Command

from app.variables_and_funcs import delete_after_delay, is_owner
from app.crud_tables.table_log_group import update_log_group
from config import bot

router = Router()

@router.message(Command("логи", prefix="!"))
async def set_log_group(message: Message):
    pass  # TODO: Commercial logic

@router.message(Command("вали", prefix="!"))
async def cmd_leave_chat(message: Message):
    pass  # TODO: Commercial logic
