from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, InputMediaAnimation
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from html import escape

from ..kbs import (
    rp_panel_ikb, rp_empty_my_ikb, rp_my_list_ikb, rp_info_ikb, global_rp_panel_ikb, rp_edit_cancel_ikb,
)
from ..variables_and_funcs import is_owner_or_chat_admin, delete_after_delay
from ..crud_tables.table_users import update_msg_count
from ..crud_tables.table_rp_cmds import get_rp_cmds_by_group_id, remove_rp_cmd, rp_cmd_exists, update_rp_cmd_gif, update_rp_cmd_text, rename_rp_cmd, create_rp_cmd
from ..crud_tables.table_rp_nsfw import (
    create_adult_rp_cmd, get_adult_rp_cmds_by_group_id,
    adult_rp_cmd_exists, remove_adult_rp_cmd,
    get_adult_rp_cmd_by_group_and_cmd, update_adult_rp_cmd_text,
    update_adult_rp_cmd_gif, rename_adult_rp_cmd,
)

from ..crud_tables.table_catalog_gifs import get_gif_from_catalog_by_id
from ..crud_tables.table_stats import update_req_count
from ..crud_tables.table_users_blacklist import is_user_in_blacklist
from ..db import db
from config import bot, logger

class RpEditWizard(StatesGroup):
    waiting_text = State()
    waiting_gif = State()
    waiting_rename = State()

router = Router()

# GLOBAL RP COMMANDS
RP_COVER_GIF_ID = "CgACAgQAAxkBAcrztWmVCDsAAdjEUo3wSzUNP8Wegm2w5gACQi4AAk-7qFBRtb6FcItonDoE"
RP_PAGE_SIZE = 8

async def _rp_user_can_manage_local(chat_id: int, user_id: int, cmd: str) -> bool:
    """Manage local RP: creator/admin only (author_id is informational)."""
    pass  # TODO: Commercial logic


@router.message(Command("грп", prefix="!"))
async def create_rp_cmd_handler(message: Message):
    pass  # TODO: Commercial logic


@router.callback_query(F.data == "adult_global_rp_cmds")
async def adult_global_rp_cmds(query: CallbackQuery):
    # 🔞 18+ убрано из глобальных. Раздел должен быть локальным (в "Мои РП").
    pass  # TODO: Commercial logic


@router.callback_query(F.data == "global_rp_cmds")
async def global_rp_cmds(query: CallbackQuery):
    pass  # TODO: Commercial logic


# RP COMMANDS
@router.message(Command("рп", prefix="!"))
async def show_local_rp_cmd(message: Message):
    pass  # TODO: Commercial logic


@router.callback_query(F.data == "rp_panel")
async def rp_panel(callback: CallbackQuery):
    pass  # TODO: Commercial logic


@router.callback_query(F.data == "rp_open_global")
async def rp_open_global(callback: CallbackQuery):
    pass  # TODO: Commercial logic


@router.callback_query(F.data.startswith("rp_my:"))
async def rp_my(callback: CallbackQuery):
    pass  # TODO: Commercial logic

@router.callback_query(F.data.startswith("rp_adult:"))
async def rp_adult(callback: CallbackQuery):
    pass  # TODO: Commercial logic

@router.callback_query(F.data.startswith("rp_info:"))
async def rp_info(callback: CallbackQuery):
    pass  # TODO: Commercial logic

@router.callback_query(F.data.startswith("rp_edit_text:"))
async def rp_edit_text(callback: CallbackQuery, state: FSMContext):
    pass  # TODO: Commercial logic


@router.callback_query(F.data.startswith("rp_edit_gif:"))
async def rp_edit_gif(callback: CallbackQuery, state: FSMContext):
    pass  # TODO: Commercial logic


@router.callback_query(F.data.startswith("rp_rename:"))
async def rp_rename(callback: CallbackQuery, state: FSMContext):
    pass  # TODO: Commercial logic


@router.message(RpEditWizard.waiting_text)
async def rp_edit_text_save(message: Message, state: FSMContext):
    pass  # TODO: Commercial logic


@router.message(RpEditWizard.waiting_gif)
async def rp_edit_gif_save(message: Message, state: FSMContext):
    pass  # TODO: Commercial logic


@router.message(RpEditWizard.waiting_rename)
async def rp_rename_save(message: Message, state: FSMContext):
    pass  # TODO: Commercial logic


# ==========================
# ✅ ДОБАВЛЕНО: НЕДОСТАЮЩИЕ CALLBACK'И (без новых функций/утилит)
# ==========================

@router.callback_query(F.data == "rp_noop")
async def rp_noop(callback: CallbackQuery):
    pass  # TODO: Commercial logic


@router.callback_query(F.data == "rp_close")
async def rp_close(callback: CallbackQuery, state: FSMContext):
    # Закрыть: удаляем сообщение панели (если можно). Если нельзя — убираем кнопки.
    pass  # TODO: Commercial logic



@router.callback_query(F.data.startswith("rp_move_to_adult:"))
async def rp_move_to_adult(callback: CallbackQuery):
    # переместить локальную (safe) команду в локальные 18+
    pass  # TODO: Commercial logic


@router.callback_query(F.data.startswith("rp_move_to_safe:"))
async def rp_move_to_safe(callback: CallbackQuery):
    # переместить локальную 18+ команду обратно в обычные локальные
    pass  # TODO: Commercial logic


@router.callback_query(F.data.startswith("rp_del:"))
async def rp_del(callback: CallbackQuery):
    pass  # TODO: Commercial logic
