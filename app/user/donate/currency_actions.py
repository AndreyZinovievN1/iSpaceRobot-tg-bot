from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter
from asyncio import sleep
import re
import time

from app.kbs import (
    choose_currency_transfer_ikb,
    confirm_currency_action_ikb,
    cancel_ikb
)
from app.variables_and_funcs import delete_after_delay

from app.crud_tables.table_users import (
    get_user_by_chat_id,
    get_user_by_username,
    update_msg_count,
    update_coins,
    update_starcoins
)

from app.crud_tables.table_stats import update_req_count
from app.crud_tables.table_users_blacklist import is_user_in_blacklist
from app.crud_tables.table_transactions import create_transaction_and_trim
from app.crud_tables.table_currency_actions import (
    add_currency_action,
    update_currency_amount,
    update_currency_type,
    delete_currency_actions,
    get_currency_action
)

from config import bot
from app.states import User

router = Router()

MIN_COINS_TRANSFER = 1000
MIN_STARCOINS_TRANSFER = 10


@router.message(Command("передать", prefix="!"))
async def transfer_cmd_handler(message: Message, state: FSMContext):
    pass  # TODO: Commercial logic


@router.callback_query(
    lambda c: c.data.startswith("coins_transfer_") or c.data.startswith("starcoins_transfer_")
)
async def choose_currency_transfer_cb(query: CallbackQuery, state: FSMContext):
    pass  # TODO: Commercial logic


@router.message(StateFilter(User.coins_transfer_amount))
async def process_coins_transfer_amount(message: Message):
    pass  # TODO: Commercial logic


@router.message(StateFilter(User.starcoins_transfer_amount))
async def process_starcoins_transfer_amount(message: Message):
    pass  # TODO: Commercial logic


@router.callback_query(lambda c: c.data.startswith("confirm_currency_action_"))
async def confirm_transfer(query: CallbackQuery):
    pass  # TODO: Commercial logic
