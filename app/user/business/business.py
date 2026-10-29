from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery, BusinessConnection, BusinessMessagesDeleted
from aiogram.filters.command import Command
from aiogram.types import Message, CallbackQuery
from aiogram.enums import ChatAction
from aiogram.filters.callback_data import CallbackData
from datetime import datetime

from app.user.business.biz_kbs import (
    choose_vip_style_ikb, get_business_ikb
)
from ...crud_tables.table_stats import update_req_count
from ...crud_tables.table_business import (
    save_business_message, update_business_message
)
from ...crud_tables.table_crm import upsert_client
from config import logger
from app.crud_tables.table_biz_ai import get_biz_ai_settings
from app.crud_tables.table_biz_connections import get_owner_id_by_conn, save_biz_connection
from app.user.business.biz_AI import is_outside_working_hours
from app.crud_tables.table_business import get_chat_history, get_message_by_id, mark_message_deleted
from app.AI import STYLING_MAP, generate_response
from app.variables_and_funcs import is_owner


class BizStyleCallback(CallbackData, prefix="biz_sty"):
    action: str  # Например: "set"
    style: str   # Например: "poetic", "science" и т.д.

router = Router()

# --- МЕНЮ И КОМАНДЫ ---

@router.message(Command("business"))
async def open_business_menu(message: Message):
    pass  # TODO: Commercial logic

@router.callback_query(F.data == "business")
async def open_business_menu(callback: CallbackQuery):
    pass  # TODO: Commercial logic

# --- ИИ И НАПОМИНАНИЯ ---

@router.message(Command("ии", prefix="!"))
async def ai_cmd_handler(message: Message):
    pass  # TODO: Commercial logic

@router.callback_query(F.data == "business_AI")
async def ai_callback_handler(callback: CallbackQuery):
    # Достаем настройки, чтобы знать статус
    pass  # TODO: Commercial logic

@router.business_message()
async def on_business_message(message: Message, bot: Bot):
    pass  # TODO: Commercial logic

@router.edited_business_message()
async def on_business_message_edited(message: Message, bot: Bot):
    pass  # TODO: Commercial logic

@router.deleted_business_messages()
async def on_business_message_deleted(event: BusinessMessagesDeleted, bot: Bot):
    pass  # TODO: Commercial logic

@router.business_connection()
async def on_business_connection(connection: BusinessConnection):
    pass  # TODO: Commercial logic
