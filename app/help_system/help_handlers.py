from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, InputMediaAnimation
from aiogram.filters.command import Command
from aiogram.exceptions import TelegramBadRequest

from ..kbs import (
    help_menu,
    admin_help_menu,
    help_menu_for_private,
    admin_help_menu_for_private,
    help_back_kb,
    subscribe_ikb
)
from .help_texts import (
    MAIN_HELP_TEXT,
    HELP_COMMANDS_TEXT,
)
from ..variables_and_funcs import is_owner_or_admin, delete_after_delay
from ..logs.logs import log_new_member
from ..crud_tables.table_users_in_private import add_user_in_private, get_user_in_private_by_chat
from ..crud_tables.table_users import (
    update_msg_count,
    count_users_with_bananas_and_coins,
    get_active_item_text_by_user
)
from ..crud_tables.table_stats import update_req_count
from ..crud_tables.table_users_blacklist import is_user_in_blacklist
from ..crud_tables.table_spamlist import get_user_from_spamlist
from ..crud_tables.table_rp_nsfw import get_all_adult_rp_cmds
from ..crud_tables.table_settings import get_total_messages_in_groups

from ..db import db
from config import bot

router = Router()

MAIN_HELP_GIF_ID = "CgACAgQAAxkBAcsGNmnUXQ29G51XG1UisPlLH_pGnZKGAAIhIAACvKepUkzFigVWD806OwQ"


async def build_main_help_text(user):
    pass  # TODO: Commercial logic


async def send_help_menu_to_user(user_id: int):
    pass  # TODO: Commercial logic


@router.message(Command("start"))
async def start_command(message: Message):
    pass  # TODO: Commercial logic


@router.message(Command("help"))
async def help_command(message: Message):
    pass  # TODO: Commercial logic


@router.callback_query(F.data == "help_commands")
async def help_commands_cb(query: CallbackQuery):
    pass  # TODO: Commercial logic


@router.callback_query(F.data == "help_status")
async def help_status_cb(query: CallbackQuery):
    pass  # TODO: Commercial logic


@router.callback_query(F.data == "help_back")
async def help_back_cb(query: CallbackQuery):
    pass  # TODO: Commercial logic
