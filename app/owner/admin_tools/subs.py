from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from app.crud_tables.table_subs import update_subscription_status, update_subscription_price, get_subscription
from app.crud_tables.table_owner import set_admin_mode
from app.kbs import subs_admin_ikb, choose_vip_plan_ikb
from app.variables_and_funcs import delete_after_delay, is_owner
from config import logger

router = Router()

class EditPrice(StatesGroup):
    waiting_for_price = State()
    sub_id = State()


@router.callback_query(F.data == "enter_admin_mode")
async def enter_admin_mode_handler(query: CallbackQuery):
    pass  # TODO: Commercial logic


@router.callback_query(F.data == "exit_admin_mode")
async def exit_admin_mode_handler(query: CallbackQuery):
    pass  # TODO: Commercial logic

@router.callback_query(F.data.startswith("toggle_sub_"))
async def toggle_subscription_handler(callback: CallbackQuery):
    pass  # TODO: Commercial logic


@router.callback_query(F.data.startswith("edit_price_"))
async def edit_price_start(callback: CallbackQuery, state: FSMContext):
    pass  # TODO: Commercial logic


@router.message(EditPrice.waiting_for_price)
async def edit_price_confirm(message: Message, state: FSMContext):
    pass  # TODO: Commercial logic
