from aiogram import Router, types
from aiogram.filters import Command
from aiogram.exceptions import TelegramBadRequest

from ..crud_tables.table_scammers import add_scammer, is_scammer, delete_scammer
from ..variables_and_funcs import is_owner_or_admin, delete_after_delay
from config import bot

router = Router()

@router.message(Command("скам", prefix="+"))
async def add_scam_cmd(message: types.Message):
    pass  # TODO: Commercial logic

@router.message(Command("скам", prefix="-"))
async def remove_scam_cmd(message: types.Message):
    pass  # TODO: Commercial logic
