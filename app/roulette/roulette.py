from aiogram import Router, F
from aiogram.types import (
    Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
)
from aiogram.filters.command import Command
import re
from datetime import datetime, timedelta
from random import randint, choice
from asyncio import sleep, Task, CancelledError
from pytz import timezone
from bs4 import BeautifulSoup
from contextlib import suppress

from app.kbs import bags_ikb, delete_ikb
from app.roulette.roulette_kbs import roulette_menu, join_roulette_menu, cancel_roulette_ikb
from app.variables_and_funcs import delete_after_delay
from app.roulette.functions import (
    recalc_tables_occupied, kick_from_roulette_after_60_sec, ROULETTE_TEXT,
    remove_user_from_roulette, spawn_roulette_task, is_roulette_shutting_down
)

from app.crud_tables.table_users import (
    get_user_by_chat_id, update_msg_count, update_coins, update_bag_cooldown,
    update_roulette_cooldown
)

from app.crud_tables.table_transactions import create_transaction_and_trim
from app.crud_tables.table_settings import get_settings_by_group_id
from app.crud_tables.table_stats import update_req_count
from app.crud_tables.table_users_blacklist import is_user_in_blacklist
from app.crud_tables.table_roulette_msgs import (
    add_roulette_msg, get_roulette_msg, update_roulette_msg_text, delete_roulette_msg
)

from config import bot
from app.lang import tr_chat

MSK_TZ = timezone("Europe/Moscow")

SPIN_TASKS: dict[int, Task] = {}
SPIN_MESSAGES: dict[int, Message] = {}
log_last_spins: list[str] = []


def clean_text(text):
    pass  # TODO: Commercial logic


router = Router()


async def open_shalosti_kb(chat_id: int) -> InlineKeyboardMarkup:
    pass  # TODO: Commercial logic


async def roulette_on_guard(event) -> bool:
    pass  # TODO: Commercial logic


@router.message(Command("рулетка", prefix="!"))
async def cmd_ban(message: Message):
    pass  # TODO: Commercial logic


@router.callback_query(F.data == "join_roulette")
async def spin_roulette(query: CallbackQuery):

    pass  # TODO: Commercial logic


@router.callback_query(
    lambda c: c.data in ["1к_1-3", "1к_4-6", "1к_7-9", "1к_10-12", "1k_on_red", "1k_on_black", "1k_on_green"]
)
async def handle_specific_bets(query: CallbackQuery):

    pass  # TODO: Commercial logic


async def do_bet(msg, user, query=None):
    pass  # TODO: Commercial logic


async def spin(query=None, message=None):
    pass  # TODO: Commercial logic


@router.callback_query(F.data.startswith("roulette_cancel:"))
async def cancel_spin_handler(query: CallbackQuery):

    pass  # TODO: Commercial logic


@router.message(Command("лог", prefix="!"))
async def show_log(message: Message):

    pass  # TODO: Commercial logic


@router.callback_query(F.data == "spin")
async def spin_roulette(query: CallbackQuery):

    pass  # TODO: Commercial logic


@router.message(Command(commands=["го", "крутить"], prefix="!"))
async def spin_message(message: Message):
    pass  # TODO: Commercial logic


@router.callback_query(F.data == "double")
async def double_bets(query: CallbackQuery):

    pass  # TODO: Commercial logic


@router.callback_query(lambda c: c.data.startswith("again"))
async def reset_user_bets(query: CallbackQuery):

    pass  # TODO: Commercial logic


@router.callback_query(lambda c: c.data.startswith("bag"))
async def random_bag(query: CallbackQuery):

    pass  # TODO: Commercial logic
