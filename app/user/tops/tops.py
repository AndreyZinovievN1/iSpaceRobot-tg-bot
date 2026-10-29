from aiogram import Router
from aiogram.types import Message, CallbackQuery

from ...lang import tr_msg
from ...variables_and_funcs import (
    delete_after_delay, is_owner_or_admin
)
from ...kbs import create_navigation_keyboard_for_spamlist, tops_panel_ikb
from ...crud_tables.table_users import (
    update_msg_count
)
from ...crud_tables.table_stats import update_req_count
from ...crud_tables.table_users_blacklist import is_user_in_blacklist
from ...db import db
from config import bot
from .nav import (
    get_spamlist_page
)

router = Router()


@router.message(lambda message: message.text == "Топ")
async def tops_panel(message: Message):
    pass  # TODO: Commercial logic


@router.callback_query(lambda c: c.data.startswith("tops_panel_"))
async def back_to_tops_panel(query: CallbackQuery):
    pass  # TODO: Commercial logic


@router.message(lambda message: message.text == "!спам")
async def spamlist_cmd(message: Message):
    pass  # TODO: Commercial logic
