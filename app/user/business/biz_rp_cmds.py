import re
from datetime import datetime
from pytz import timezone

from aiogram import Router, F, Bot, html
from aiogram.types import Message, CallbackQuery, InlineKeyboardButton
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.filters.biz_rp_filter import IsBusinessRP
from app.crud_tables.table_business_rp_cmds import (
    create_business_rp_cmd,
    remove_business_rp_cmd,
    get_business_rp_cmds,
)
from app.crud_tables.table_catalog_gifs import get_gif_from_catalog_by_id
from app.crud_tables.table_vip_users import get_vip_user

router = Router()

BIZRP_PAGE_SIZE = 8
MSK_TZ = timezone("Europe/Moscow")

CATALOG_LINK = "<a href='https://t.me/catalog_iSpace'>Каталог Space ✨</a>"

# ✅ ID владельца (для приватного каталога GIF)
OWNER_ID = 0  # TODO: Commercial logic

# ✅ чтобы не спамить подсказкой в чатах каждую секунду
_VIP_HINT_COOLDOWN: dict[tuple[int, int], datetime] = {}  # (chat_id, user_id) -> last_dt


class BizRpWizard(StatesGroup):
    waiting_cmd = State()
    waiting_text = State()
    waiting_gif = State()


def _normalize_cmd(cmd: str) -> str:
    pass  # TODO: Commercial logic


def _safe_gif_preview(gif_id: str | None) -> str:
    pass  # TODO: Commercial logic


def _paginate(total: int, page: int):
    pass  # TODO: Commercial logic


def _render_my_list_text(total: int, page: int, pages: int, start: int, end: int):
    pass  # TODO: Commercial logic


def _build_my_list_kb(rows, page: int):
    pass  # TODO: Commercial logic


def _build_info_text(cmd: str, text_cmd: str, gif_id: str | None):
    pass  # TODO: Commercial logic


def _build_info_kb(cmd: str, page: int):
    pass  # TODO: Commercial logic


async def _is_vip_active(user_id: int) -> bool:
    pass  # TODO: Commercial logic


def _build_caption_with_catalog(text: str, is_vip: bool) -> str:
    # VIP -> без каталога, не VIP -> с каталогом
    pass  # TODO: Commercial logic


def _user_link(user_id: int, full_name: str) -> str:
    pass  # TODO: Commercial logic


def _render_bizrp_text(rp_data: dict, me_id: int, me_name: str, target_id: int, target_name: str) -> str:
    pass  # TODO: Commercial logic


async def _send_vip_needed_hint(message: Message):
    """
    Показать подсказку в чате (и не спамить).
    """
    pass  # TODO: Commercial logic


@router.callback_query(F.data == "bizrp_vip_help")
async def bizrp_vip_help(callback: CallbackQuery):
    pass  # TODO: Commercial logic


# --- 1A. BUSINESS CONNECTION (если используешь) ---
@router.business_message(IsBusinessRP())
async def business_rp_handler(message: Message, rp_data: dict, bot: Bot):
    pass  # TODO: Commercial logic


# --- 1B. ✅ Обычные сообщения (ЛС + чаты) ---
@router.message(IsBusinessRP())
async def business_rp_handler_normal(message: Message, rp_data: dict, bot: Bot):
    pass  # TODO: Commercial logic


# --- 2. МЕНЮ УПРАВЛЕНИЯ РП-КОМАНДАМИ ---
@router.callback_query(F.data == "business_rp_cmds")
async def handle_rp_menu(callback: CallbackQuery):
    pass  # TODO: Commercial logic


@router.callback_query(F.data == "bizrp_noop")
async def bizrp_noop(callback: CallbackQuery):
    pass  # TODO: Commercial logic


@router.callback_query(F.data.startswith("bizrp_my:"))
async def bizrp_my(callback: CallbackQuery):
    pass  # TODO: Commercial logic


@router.callback_query(F.data.startswith("bizrp_info:"))
async def bizrp_info(callback: CallbackQuery):
    pass  # TODO: Commercial logic


@router.callback_query(F.data == "bizrp_close_info")
async def bizrp_close_info(callback: CallbackQuery):
    pass  # TODO: Commercial logic


@router.callback_query(F.data.startswith("bizrp_delinfo:"))
async def bizrp_delinfo(callback: CallbackQuery):
    pass  # TODO: Commercial logic


@router.callback_query(F.data.startswith("bizrp_del:"))
async def bizrp_del(callback: CallbackQuery):
    pass  # TODO: Commercial logic


@router.message(Command("бизрп", prefix="+"))
async def fast_create_biz_rp(message: Message):
    pass  # TODO: Commercial logic


@router.message(Command("бизрп", prefix="-"))
async def delete_biz_rp(message: Message):
    pass  # TODO: Commercial logic


@router.callback_query(F.data == "start_biz_wizard")
async def start_biz_rp_wizard(callback: CallbackQuery, state: FSMContext):
    pass  # TODO: Commercial logic


@router.message(BizRpWizard.waiting_cmd)
async def wizard_cmd(message: Message, state: FSMContext):
    pass  # TODO: Commercial logic


@router.message(BizRpWizard.waiting_text)
async def wizard_text(message: Message, state: FSMContext):
    pass  # TODO: Commercial logic


@router.message(BizRpWizard.waiting_gif)
async def wizard_gif(message: Message, state: FSMContext):
    pass  # TODO: Commercial logic


@router.callback_query(F.data == "cancel_rp_wizard")
async def cancel_wizard(callback: CallbackQuery, state: FSMContext):
    pass  # TODO: Commercial logic
