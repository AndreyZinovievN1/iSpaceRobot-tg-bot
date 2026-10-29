from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, LabeledPrice, PreCheckoutQuery
from aiogram.filters.command import Command
import re
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from pytz import timezone
from dateutil.parser import isoparse
from aiogram.fsm.context import FSMContext
from aiogram.exceptions import TelegramBadRequest
from contextlib import suppress
import math

from ..kbs import (
    delete_ikb, profile_ikb, transactions_delete_ikb, choose_vip_plan_ikb,
    profile_settings_ikb, donate_ikb
)
from ..variables_and_funcs import is_owner, is_admin, is_chat_creator, delete_after_delay
from ..logs.logs import log_buying_vip, log_cancel_last_transaction
from ..crud_tables.table_marriages import get_marriage
from ..crud_tables.table_users import update_msg_count, get_user_by_chat_id, update_starcoins
from ..crud_tables.table_stats import update_req_count
from ..crud_tables.table_users_blacklist import is_user_in_blacklist, get_user_from_blacklist
from ..crud_tables.table_spamlist import get_user_from_spamlist
from ..crud_tables.table_transactions import (
    get_user_transactions, get_last_transaction_by_user,
    update_last_transaction, create_transaction_and_trim,
    count_user_transactions
)
from ..crud_tables.table_vip_users import get_vip_user, add_vip_user, update_vip_expiry
from ..crud_tables.table_profile_settings import (
    get_profile_settings_by_user_id, add_profile_settings, update_profile_settings
)
from ..crud_tables.table_subs import get_subscription
from app.crud_tables.table_owner import get_admin_mode, set_admin_mode
from ..db import db
from config import bot
from ..lang import tr_msg, get_tr

MSK_TZ = timezone("Europe/Moscow")
TX_PER_PAGE = 5

def _format_dt_msk(tx) -> str:
    """
    created_at в БД обычно timestamptz (UTC).
    Здесь всегда приводим к МСК и форматируем красиво.
    """
    pass  # TODO: Commercial logic

router = Router()

@router.message(Command("donate"))
async def donate_cmd(message: Message):
    pass  # TODO: Commercial logic
    
async def profile_cmd(message: Message, user, is_callback: bool = False):
    pass  # TODO: Commercial logic

@router.message(Command("проф", prefix="!"))
async def profile_cmd_handler(message: Message):
    pass  # TODO: Commercial logic

@router.callback_query(F.data == "profile")
async def profile_cmd_callback(query: CallbackQuery, state: FSMContext):
    pass  # TODO: Commercial logic

@router.callback_query(lambda c: c.data.startswith("buy_sub_"))
async def choose_subscription(query: CallbackQuery):
    pass  # TODO: Commercial logic

async def grant_vip_subscription(user_id: int, months: int):
    """Общая логика начисления VIP подписки"""
    pass  # TODO: Commercial logic


@router.callback_query(F.data == "toggle_admin_mode")
async def toggle_admin_mode_handler(query: CallbackQuery):
    pass  # TODO: Commercial logic

@router.callback_query(lambda c: c.data.startswith("admin_give_sub_"))
async def admin_give_vip_callback(query: CallbackQuery):
    # Парсим: admin_give_sub_{sub_id}_{user_id}
    pass  # TODO: Commercial logic

@router.callback_query(lambda c: c.data.startswith("get_vip_sub_"))
async def buy_vip_plan(query: CallbackQuery):
    pass  # TODO: Commercial logic
    
@router.message(F.successful_payment)
async def process_successful_payment(message: Message):
    pass  # TODO: Commercial logic


@router.callback_query(F.data == "buy_vip")
async def buy_vip(query: CallbackQuery) -> None:
    pass  # TODO: Commercial logic

@router.callback_query(lambda c: c.data.startswith("profile_settings_"))
async def command_donate_handler(query: CallbackQuery) -> None:
    pass  # TODO: Commercial logic

@router.callback_query(F.data.contains("_profile_info_"))
async def profile_info(query: CallbackQuery):
    pass  # TODO: Commercial logic


@router.callback_query(F.data.contains("_profile_settings_"))
async def profile_toggle(query: CallbackQuery):
    pass  # TODO: Commercial logic



@router.callback_query(lambda c: c.data.startswith("transactions_"))
async def transactions_list(query: CallbackQuery):
    # formats:
    # transactions_{user}
    # transactions_{user}_{page}
    pass  # TODO: Commercial logic

    
# @router.callback_query(lambda c: c.data.startswith("cancel_last_transaction_"))
# async def command_refund_handler(query: CallbackQuery) -> None:
#     match = re.search(r"cancel_last_transaction_(\d+)", query.data)
#     if match:
#         user_id = int(match.group(1))
#         if user_id != query.from_user.id:
#             return
        
#     transaction = await get_last_transaction_by_user(query.from_user.id)

#     try:
#         await remove_vip_user(query.from_user.id)
#         await bot.refund_star_payment(
#             user_id=query.from_user.id,
#             telegram_payment_charge_id=transaction['transaction_id']
#         )
#         transaction = await get_last_transaction_by_user(query.from_user.id, True)
#         await log_cancel_last_transaction(query.from_user, transaction["stars_amount"])
#         await update_transaction_canceled(transaction['transaction_id'], True)
#         await query.answer("✅ Возврат успешно выполнен!", show_alert=True)
#     except Exception as e:
#         await query.answer("❌ Ошибка при возврате платежа", show_alert=True)
#         print(e)



@router.callback_query(lambda c: c.data.startswith("mutedList_"))
async def set_day(query: CallbackQuery):
    pass  # TODO: Commercial logic
