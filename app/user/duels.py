from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters.command import Command
from random import choice, randint
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter
import re
from asyncio import sleep
from datetime import datetime
from pytz import timezone

from ..kbs import (
    confirm_duel_ikb, started_duel_ikb, cancel_ikb
)
from ..variables_and_funcs import (
    delete_after_delay
)
from ..logs.logs import (
    log_new_member
)
from ..crud_tables.table_users_in_private import (
    add_user_in_private, get_user_in_private_by_chat
)
from ..crud_tables.table_users import get_user_by_chat_id, update_msg_count, update_coins
from ..crud_tables.table_stats import update_req_count
from ..crud_tables.table_users_blacklist import is_user_in_blacklist
from ..crud_tables.table_duels import (
    add_duel, get_duel, remove_duel, update_hp, update_phaser_temp,
    update_maneuver_and_shield, update_shield_hp, update_energy, update_prize
)
from ..crud_tables.table_transactions import create_transaction_and_trim

from config import bot
from ..states import User
from ..lang import tr_chat

router = Router()

MSK_TZ = timezone("Europe/Moscow")


def tg_link(uid: int, name: str) -> str:
    pass  # TODO: Commercial logic


async def get_duel_text(chat_id: int, duel, next_attacker, result_of_actions: str | None = None) -> str:

    pass  # TODO: Commercial logic


def legacy_get_duel_text(duel, next_attacker, result_of_actions=None):
    pass  # TODO: Commercial logic


def extract_duel_data(duel, user_prefix: str):
    pass  # TODO: Commercial logic


@router.message(Command("дуэль", prefix="!"))
async def start_duel(message: Message, state: FSMContext):
    pass  # TODO: Commercial logic


@router.message(StateFilter(User.bet_on_duel))
async def process_name(message: Message, state: FSMContext) -> None:
    pass  # TODO: Commercial logic


@router.callback_query(lambda c: c.data.startswith("duel_confirm_"))
async def start_duel(query: CallbackQuery):
    pass  # TODO: Commercial logic


@router.callback_query(lambda c: c.data.startswith("run_from_duel_"))
async def run_from_duel(query: CallbackQuery):
    pass  # TODO: Commercial logic


@router.callback_query(lambda c: c.data.startswith("give_up_duel_"))
async def give_up_duel(query: CallbackQuery):
    pass  # TODO: Commercial logic


@router.callback_query(lambda c: c.data.startswith("guide"))
async def guide(query: CallbackQuery):
    pass  # TODO: Commercial logic


@router.callback_query(lambda c: c.data.startswith("phaser_duel_"))
async def run_from_duel(query: CallbackQuery):
    pass  # TODO: Commercial logic


@router.callback_query(lambda c: c.data.startswith("maneuver_duel_"))
async def run_from_duel(query: CallbackQuery):
    pass  # TODO: Commercial logic


@router.callback_query(lambda c: c.data.startswith("shield_duel_"))
async def run_from_duel(query: CallbackQuery):
    pass  # TODO: Commercial logic
