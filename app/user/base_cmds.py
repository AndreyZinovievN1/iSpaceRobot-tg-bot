from aiogram import Router, F
from aiogram.types import InlineKeyboardMarkup, Message, CallbackQuery, InaccessibleMessage, InlineKeyboardButton, WebAppInfo
from aiogram.filters.command import Command
from aiogram.exceptions import TelegramBadRequest
import re
from datetime import datetime, timedelta
from random import randint
from pytz import timezone
from aiogram.fsm.context import FSMContext

from ..kbs import (
    delete_ikb, stats_ikb,
    subscribe_ikb, user_lang_menu_ikb
)
from ..variables_and_funcs import (
    is_owner_or_admin, is_owner, is_owner_or_chat_admin,
    delete_after_delay
)
from ..logs.logs import log_new_member
from ..crud_tables.table_users_in_private import (
    add_user_in_private, get_user_in_private_by_chat
)
from ..crud_tables.table_users import (
    get_user_by_chat_id, get_user_by_username,
    update_banana, update_msg_count, update_banana_cooldown,
    count_users_with_bananas_and_coins, get_count_of_users, update_lang,
    get_active_item_text_by_user
)
from ..crud_tables.table_allowed_links import get_allowed_links_by_group_id
from ..crud_tables.table_stats import update_req_count
from ..crud_tables.table_settings import get_settings_by_group_id
from ..crud_tables.table_stops import add_stop, get_stop, delete_stop
from ..crud_tables.table_users_blacklist import is_user_in_blacklist
from ..crud_tables.table_duels import get_duel, remove_duel
from ..crud_tables.table_rp_nsfw import get_all_adult_rp_cmds
from ..crud_tables.table_settings import get_total_messages_in_groups
from ..db import db
from config import bot, logger
from ..lang import tr_msg, get_tr
from ..help_system.help_handlers import send_help_menu_to_user

router = Router()

LANG_NAMES = {"ru": "Русский", "ua": "Українська", "en": "English"}


@router.callback_query(F.data == "user_lang_open")
async def user_lang_open(cb: CallbackQuery):
    pass  # TODO: Commercial logic


@router.callback_query(F.data.startswith("lang:set:user:"))
async def user_lang_set(cb: CallbackQuery):
    pass  # TODO: Commercial logic


@router.callback_query(F.data == "check_subscribe")
async def settings(query: CallbackQuery):
    pass  # TODO: Commercial logic


@router.message(Command("start"))
async def start_command(message: Message):
    pass  # TODO: Commercial logic


@router.message(Command("id"))
async def start_command_id(message: Message):
    pass  # TODO: Commercial logic


async def cosmos_cmd(message: Message, user, *, edit_message: bool = False):
    pass  # TODO: Commercial logic


@router.message(Command("космос", prefix="!"))
async def cmd_ban(message: Message):
    pass  # TODO: Commercial logic


@router.callback_query(F.data == "cosmos")
async def cmd_ban_cb(query: CallbackQuery, state: FSMContext):
    pass  # TODO: Commercial logic


@router.message(Command("банан", prefix="!"))
async def back_to_main_menu_handler(message: Message):
    pass  # TODO: Commercial logic


@router.message(Command("агенты", prefix="!"))
async def admins_list(message: Message):
    pass  # TODO: Commercial logic


@router.message(Command("ссылки", prefix="!"))
async def show_allowed_links(message: Message):
    pass  # TODO: Commercial logic


@router.message(Command("стоп", prefix="!"))
async def cmd_ban_stop(message: Message):
    pass  # TODO: Commercial logic


@router.callback_query(lambda c: c.data.startswith("deleteMessage"))
async def set_day(query: CallbackQuery, state: FSMContext):
    pass  # TODO: Commercial logic

@router.message(Command("bot"))
async def cmd_bot(message: Message):
    pass  # TODO: Commercial logic
