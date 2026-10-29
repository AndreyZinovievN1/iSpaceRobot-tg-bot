from datetime import datetime
from html import escape
from pathlib import Path

from aiogram import Router, Bot
from aiogram.enums import ChatAction
from aiogram.types import Message, BusinessConnection, BusinessMessagesDeleted

from config import logger
from app.AI import STYLING_MAP, generate_response
from app.crud_tables.table_biz_ai import get_biz_ai_settings
from app.crud_tables.table_biz_connections import get_owner_id_by_conn, save_biz_connection
from app.crud_tables.table_business import (
    save_business_message,
    update_business_message,
    get_chat_history,
    get_message_by_id,
    mark_message_deleted,
)
from app.crud_tables.table_crm import upsert_client
from app.user.business.biz_AI import is_outside_working_hours

router = Router()

ALLOWED_OWNER_IDS: list[int] = []  # TODO: Commercial logic
DELETED_MEDIA_DIR = Path("business_deleted_media")


def build_user_meta(old_msg_data: dict | None = None, message: Message | None = None) -> tuple[str, str]:
    pass  # TODO: Commercial logic


def extract_business_content(message: Message) -> dict:
    pass  # TODO: Commercial logic


def media_ext(content_type: str) -> str:
    pass  # TODO: Commercial logic


async def try_preload_media(bot: Bot, file_id: str | None, content_type: str, msg_id: int) -> str | None:
    pass  # TODO: Commercial logic


def quote_block(text: str) -> str:
    pass  # TODO: Commercial logic


def build_header(title: str, clickable_name: str, user_code: str) -> str:
    pass  # TODO: Commercial logic


async def send_deleted_business_content(bot: Bot, owner_id: int, old_msg_data: dict):
    pass  # TODO: Commercial logic


@router.business_message()
async def on_business_message(message: Message, bot: Bot):
    pass  # TODO: Commercial logic


@router.edited_business_message()
async def on_business_message_edited(message: Message, bot: Bot):
    pass  # TODO: Commercial logic


@router.deleted_business_messages()
async def on_business_message_deleted(event: BusinessMessagesDeleted, bot: Bot):
    pass  # TODO: Commercial logic


@router.business_connection()
async def on_business_connection(connection: BusinessConnection):
    pass  # TODO: Commercial logic
