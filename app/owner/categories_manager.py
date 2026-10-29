from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.fsm.context import FSMContext

from app.kbs import cancel_ikb
from app.crud_tables.table_shop_items import (
    get_shop_items_by_category, get_item_info, add_shop_item, remove_shop_item
)
from app.states import ShopAdmin
from app.user.donate.categories import render_category_page
from app.variables_and_funcs import is_owner

router = Router()


def parse_category_item_callback(callback_data: str, prefix: str):
    """
    Работает с категориями, где есть нижнее подчёркивание:
    conf_del_emojis_87 -> category=emojis, item_id=87
    conf_del_premium_emojis_87 -> category=premium_emojis, item_id=87
    execute_del_chart_skin_anime_87 -> category=chart_skin_anime, item_id=87
    """
    pass  # TODO: Commercial logic


@router.callback_query(F.data.startswith("admin_add_"))
async def admin_add_start(callback: CallbackQuery, state: FSMContext):
    pass  # TODO: Commercial logic


@router.message(ShopAdmin.waiting_for_text_m)
async def admin_set_m(message: Message, state: FSMContext):
    pass  # TODO: Commercial logic


@router.message(ShopAdmin.waiting_for_text_f)
async def admin_set_f(message: Message, state: FSMContext):
    pass  # TODO: Commercial logic


@router.message(ShopAdmin.waiting_for_price)
async def admin_set_price(message: Message, state: FSMContext):
    pass  # TODO: Commercial logic


@router.callback_query(F.data.startswith("sw_"))
async def switch_gender_view(callback: CallbackQuery):
    pass  # TODO: Commercial logic


@router.callback_query(F.data.startswith("admin_delete_"))
async def admin_delete_list(callback: CallbackQuery):
    pass  # TODO: Commercial logic


@router.callback_query(F.data.startswith("conf_del_"))
async def admin_confirm_delete(callback: CallbackQuery):
    pass  # TODO: Commercial logic


@router.callback_query(F.data.startswith("execute_del_"))
async def admin_execute_delete(callback: CallbackQuery):
    pass  # TODO: Commercial logic


async def refresh_admin_delete_list(callback: CallbackQuery, category: str):
    pass  # TODO: Commercial logic
