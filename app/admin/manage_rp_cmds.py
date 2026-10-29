from aiogram import Router, F, html
from aiogram.types import Message, CallbackQuery
from aiogram.filters.command import Command
from aiogram.filters import StateFilter
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
import re
from contextlib import suppress

from ..lang import tr_msg

from ..kbs import delete_ikb_like_back, rp_create_choose_type_ikb, rp_wizard_gif_step_ikb
from ..variables_and_funcs import (
    is_owner_or_admin, delete_after_delay, is_chat_admin, is_chat_creator
)
from ..crud_tables.table_users import update_msg_count
from ..crud_tables.table_users_blacklist import is_user_in_blacklist
from ..crud_tables.table_rp_cmds import create_rp_cmd, rp_cmd_exists, remove_rp_cmd
from ..crud_tables.table_stats import update_req_count
from ..crud_tables.table_global_rp_cmds import global_rp_cmd_exists
from ..crud_tables.table_rp_nsfw import create_adult_rp_cmd
from ..crud_tables.table_catalog_gifs import get_gif_from_catalog_by_id
from config import bot


CATALOG_CHAT_ID = 0  # TODO: Commercial logic


class CreateLocalRpWizard(StatesGroup):
    waiting_type = State()
    waiting_cmd = State()
    waiting_text = State()
    waiting_gif = State()  # оставили для совместимости, но в визарде больше не используем


router = Router()


@router.message(Command("рп", prefix="+"))
async def create_local_rp_cmd_handler(message: Message, state: FSMContext):
    pass  # TODO: Commercial logic


@router.callback_query(StateFilter(CreateLocalRpWizard.waiting_type), F.data == "rp_create:cancel")
async def rp_create_cancel_cb(call: CallbackQuery, state: FSMContext):
    pass  # TODO: Commercial logic


@router.callback_query(StateFilter(CreateLocalRpWizard.waiting_type), F.data.in_({"rp_create:type:normal", "rp_create:type:adult"}))
async def rp_create_type_cb(call: CallbackQuery, state: FSMContext):
    pass  # TODO: Commercial logic


@router.message(StateFilter(CreateLocalRpWizard.waiting_cmd))
async def rp_wizard_cmd(message: Message, state: FSMContext):
    pass  # TODO: Commercial logic


@router.message(StateFilter(CreateLocalRpWizard.waiting_text))
async def rp_wizard_text(message: Message, state: FSMContext):
    pass  # TODO: Commercial logic


@router.callback_query(F.data == "rpwiz:cancel")
async def rp_wizard_cancel_btn(call: CallbackQuery, state: FSMContext):
    # Отмена визарда кнопкой
    pass  # TODO: Commercial logic


@router.callback_query(F.data == "rpwiz:back_text")
async def rp_wizard_back_to_text(call: CallbackQuery, state: FSMContext):
    # Назад на шаг текста
    pass  # TODO: Commercial logic


@router.callback_query(F.data == "rpwiz:skip_gif")
async def rp_wizard_skip_gif(call: CallbackQuery, state: FSMContext):
    # Создать команду без GIF
    pass  # TODO: Commercial logic


@router.message(StateFilter(CreateLocalRpWizard.waiting_gif))
async def rp_wizard_gif(message: Message, state: FSMContext):
    # В шаге GIF принимаем ТОЛЬКО ID из каталога (сообщения с GIF файлами не принимаем)
    pass  # TODO: Commercial logic


@router.message(StateFilter("*"), F.text.casefold() == "отмена")
async def rp_wizard_cancel_any(message: Message, state: FSMContext):
    pass  # TODO: Commercial logic


@router.message(Command("рп", prefix="-"))
async def delete_local_rp_cmd_handler(message: Message):
    pass  # TODO: Commercial logic
