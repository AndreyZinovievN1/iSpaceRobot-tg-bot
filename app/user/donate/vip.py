from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters.command import Command
import re
from datetime import datetime, timedelta
from pytz import timezone
from aiogram.exceptions import TelegramBadRequest
from contextlib import suppress
import math
from typing import Optional, Tuple

from app.user.donate.donate_kbs import choose_vip_plan_ikb, donate_ikb
from app.variables_and_funcs import is_owner
from app.logs.logs import log_buying_vip
from app.crud_tables.table_users import get_user_by_chat_id, update_starcoins
from app.crud_tables.table_transactions import (
    get_last_transaction_by_user, update_last_transaction, create_transaction_and_trim,
)
from app.crud_tables.table_vip_users import get_vip_user, add_vip_user, remove_vip_user, update_vip_expiry
from app.crud_tables.table_subs import get_subscription
from app.crud_tables.table_owner import get_admin_mode, set_admin_mode
from app.lang import tr_msg

router = Router()

@router.callback_query(lambda c: c.data.startswith("buy_sub_"))
async def choose_subscription(query: CallbackQuery):
    pass  # TODO: Commercial logic


async def grant_vip_subscription(user_id: int, months: int):
    pass  # TODO: Commercial logic


@router.callback_query(F.data == "toggle_admin_mode")
async def toggle_admin_mode_handler(query: CallbackQuery):
    pass  # TODO: Commercial logic


@router.callback_query(lambda c: c.data.startswith("admin_give_sub_"))
async def admin_give_vip_callback(query: CallbackQuery):
    pass  # TODO: Commercial logic


@router.callback_query(F.data.startswith("admin_remove_vip_"))
async def admin_remove_vip_callback(query: CallbackQuery):
    pass  # TODO: Commercial logic


@router.callback_query(lambda c: c.data.startswith("get_vip_sub_"))
async def buy_vip_plan(query: CallbackQuery):
    pass  # TODO: Commercial logic


@router.callback_query(F.data == "buy_vip")
async def buy_vip(query: CallbackQuery) -> None:
    pass  # TODO: Commercial logic
