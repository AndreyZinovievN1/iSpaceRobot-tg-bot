from aiogram import Router, F, html
from aiogram.types import Message
from aiogram.filters.command import Command
from aiogram.exceptions import (
    TelegramMigrateToChat, TelegramForbiddenError, TelegramNotFound
)
import time
from asyncio import sleep
from random import uniform
from aiogram.types import InputMediaPhoto, InputMediaVideo, FSInputFile
from aiogram_media_group import media_group_handler
from typing import List
from fpdf import FPDF
from datetime import datetime
import os
from pytz import timezone
import re
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton
from aiogram.utils import text_decorations

from app.crud_tables.table_chat_owners import get_chat_owner_by_chat_id
from app.crud_tables.table_vip_users import get_vip_user
from app.variables_and_funcs import is_owner, delete_after_delay
from app.logs.logs import (
    log_broadcast_error,
    log_broadcast_successfully, log_broadcast_error_not_found
)
from app.crud_tables.table_users import update_msg_count
from app.crud_tables.table_stats import update_req_count
from app.crud_tables.table_settings import remove_settings, update_settings
from app.crud_tables.table_admins import get_admin_by_chat
from app.crud_tables.table_ad_group import update_ad_group
from app.crud_tables.table_owner import update_gallery, get_gallery, delete_gallery
from app.db import db
from config import bot

router = Router()

def save_pdf(filename: str, bg_path: str, text: str):
    pass  # TODO: Commercial logic

def parse_buttons_from_text(text: str):
    # 1. Ищем кнопки в формате [Текст [ссылка]]
    pass  # TODO: Commercial logic

@router.message(F.media_group_id, F.content_type.in_({'photo', 'video'}))
@media_group_handler
async def on_media_group(messages: List[Message]):
    pass  # TODO: Commercial logic

@router.message(Command("рассылка", prefix="!"))
async def cmd_broadcast(message: Message):
    pass  # TODO: Commercial logic

@router.message(Command("реклама", prefix="!"))
async def add_moder_for_group(message: Message):
    pass  # TODO: Commercial logic

@router.message(Command("html"))
async def cmd_broadcast(message: Message):
    pass  # TODO: Commercial logic
