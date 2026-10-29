import asyncio
from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery, InlineKeyboardButton
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from ...crud_tables.table_vip_users import get_vip_user
from ...crud_tables.table_crm import get_all_client_ids

router = Router()

# Состояния для рассылки
class BroadcastStates(StatesGroup):
    waiting_for_message = State()
    confirm = State()

# 1. Вход в режим рассылки
@router.callback_query(F.data == "business_broadcast")
async def start_broadcast(callback: CallbackQuery, state: FSMContext):
    pass  # TODO: Commercial logic

# 2. Получение сообщения и запрос подтверждения
@router.message(BroadcastStates.waiting_for_message)
async def process_broadcast_content(message: Message, state: FSMContext):
    # Сохраняем сообщение для последующей пересылки
    pass  # TODO: Commercial logic

# 3. Выполнение рассылки
@router.callback_query(BroadcastStates.confirm, F.data == "confirm_broadcast")
async def run_broadcast(callback: CallbackQuery, state: FSMContext, bot: Bot):
    pass  # TODO: Commercial logic

# Отмена рассылки
@router.callback_query(F.data == "cancel_broadcast")
async def cancel_broadcast(callback: CallbackQuery, state: FSMContext):
    pass  # TODO: Commercial logic
