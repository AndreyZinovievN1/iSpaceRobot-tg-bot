from aiogram import Router, F
from aiogram.types import CallbackQuery
import math

# Импортируем методы из твоего файла базы
from app.crud_tables.table_business import get_business_clients, get_chat_history_paged 
from app.user.business.biz_kbs import (
    get_clients_kb, get_history_kb, ClientsCallback, HistoryCallback
)

router = Router()

@router.callback_query(ClientsCallback.filter())
async def show_clients_list(callback: CallbackQuery, callback_data: ClientsCallback):
    pass  # TODO: Commercial logic

@router.callback_query(HistoryCallback.filter())
async def show_chat_history(callback: CallbackQuery, callback_data: HistoryCallback):
    pass  # TODO: Commercial logic
