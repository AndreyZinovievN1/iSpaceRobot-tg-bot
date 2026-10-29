from aiogram import Router, F
from aiogram.types import Message, ChatMemberUpdated, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import ChatMemberUpdatedFilter, IS_NOT_MEMBER, IS_MEMBER
from aiogram.enums import ChatMemberStatus
from datetime import datetime
from pytz import timezone
import re
import time
from random import choice

from .variables_and_funcs import (
    delete_after_delay, is_owner, is_owner_or_admin,
    reaction_to_owner_pins, reaction_to_pin, reaction_to_pin_in_night, is_chat_admin,
    get_group_owner, is_admin, apply_replacements, get_reaction
)
from .logs.logs import (
    log_new_group, log_bot_kicked
)
from .crud_tables.table_groups_blacklist import is_group_in_blacklist
from .crud_tables.table_settings import (
    add_settings, get_settings_by_group_id
)
from .crud_tables.table_chat_owners import get_chat_owner_by_chat_id
from .crud_tables.table_admins import get_admin_by_chat
from .crud_tables.table_banlist import is_user_in_banlist
from .crud_tables.table_spamlist import get_user_from_spamlist
from .crud_tables.table_users import get_active_item_text_by_user
from .logs.logs import log_banlist_user
from config import bot, logger
from .db import db
from .lang import tr_chat

router = Router()

_SPAM_NOTICE_COOLDOWN = {}
_SPAM_NOTICE_TTL = 15


def _build_user_link(user) -> str:
    pass  # TODO: Commercial logic


def _spam_reason_from_entry(spam_entry) -> str:
    pass  # TODO: Commercial logic


def _spam_notice_key(chat_id: int, user_id: int):
    pass  # TODO: Commercial logic


def _can_send_spam_notice(chat_id: int, user_id: int) -> bool:
    pass  # TODO: Commercial logic


def _is_animation_rights_error(exc: Exception) -> bool:
    pass  # TODO: Commercial logic


def _is_text_rights_error(exc: Exception) -> bool:
    pass  # TODO: Commercial logic


async def safe_send_animation(
    *,
    chat_id: int,
    animation: str,
    caption: str,
):
    pass  # TODO: Commercial logic


async def send_spamlist_block_message(chat_id: int, user, spam_entry=None):
    pass  # TODO: Commercial logic


async def send_banlist_block_message(chat_id: int, user):
    pass  # TODO: Commercial logic


async def block_user_with_spam_notice(chat_id: int, user_id: int, user_obj=None, spam_entry=None):
    pass  # TODO: Commercial logic


@router.my_chat_member(ChatMemberUpdatedFilter(member_status_changed=IS_NOT_MEMBER >> IS_MEMBER))
async def on_bot_added(event: ChatMemberUpdated):
    pass  # TODO: Commercial logic


@router.my_chat_member() 
async def on_my_chat_member(update: ChatMemberUpdated):
    pass  # TODO: Commercial logic


@router.chat_member()
async def greet_on_join(event: ChatMemberUpdated):
    pass  # TODO: Commercial logic


@router.chat_member()
async def on_spamlisted_user_kicked(event: ChatMemberUpdated):
    pass  # TODO: Commercial logic


@router.message(F.new_chat_members)
async def somebody_added(message: Message):
    pass  # TODO: Commercial logic


@router.message(F.left_chat_member)
async def somebody_removed(message: Message):
    pass  # TODO: Commercial logic


@router.message(F.pinned_message)
async def handle_pinned_message(message: Message):
    pass  # TODO: Commercial logic


@router.message(F.content_type == "new_chat_title")
async def title_changed(message: Message):
    pass  # TODO: Commercial logic


@router.message(F.content_type == "new_chat_photo")
async def photo_changed(message: Message):
    pass  # TODO: Commercial logic
