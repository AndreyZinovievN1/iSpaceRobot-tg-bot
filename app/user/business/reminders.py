from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery, InlineKeyboardButton
from aiogram.filters.command import Command, CommandObject
from aiogram.utils.keyboard import InlineKeyboardBuilder
import re
from datetime import datetime, timedelta
from pytz import timezone
from typing import Optional

# Импортируем шедулер из твоего конфига
from config import scheduler 

router = Router()

# --- ТВОЙ ПАРСЕР ---

def parse_time(time_string: Optional[str]) -> Optional[datetime]:
    pass  # TODO: Commercial logic

# --- ФУНКЦИЯ ОТПРАВКИ ---

@router.callback_query(F.data == "business_reminders")
async def business_reminders_info(callback: CallbackQuery):
    # Короткий и понятный текст для всплывающего окна
    pass  # TODO: Commercial logic

async def send_reminder_callback(bot: Bot, user_id: int, text: str):
    pass  # TODO: Commercial logic

# --- ХЕНДЛЕРЫ ---

@router.message(Command("remind"))
async def create_reminder(message: Message, command: CommandObject, bot: Bot):
    # Здесь должна быть твоя проверка на VIP
    # if not user.is_vip: ...
    
    pass  # TODO: Commercial logic

@router.message(Command("reminders"))
async def list_reminders(message: Message):
    pass  # TODO: Commercial logic

@router.callback_query(F.data.startswith("del_rem_"))
async def delete_reminder(callback: CallbackQuery):
    pass  # TODO: Commercial logic
