from aiogram import Router, F
from aiogram.types import Message

from app.variables_and_funcs import (
    get_chat_creator
)
from app.crud_tables.table_channels_to_control import (
    add_channel_to_control, get_channel_to_control, update_channels_to_control,
    get_channels_by_owner
)
from .lang import tr_chat
from app.db import db
from config import bot

router = Router()

async def send_channel_report(channel):
    """Вспомогательная функция для формирования и отправки отчета в ЛС"""
    pass  # TODO: Commercial logic

async def check_channel_subs():
    pass  # TODO: Commercial logic

@router.message(F.text == "!канал")
async def handle_channel_command(message: Message):
    pass  # TODO: Commercial logic

@router.channel_post()
async def handle_channel_post(message: Message):
    pass  # TODO: Commercial logic
