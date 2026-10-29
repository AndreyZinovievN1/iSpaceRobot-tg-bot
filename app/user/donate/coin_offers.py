from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
import re
from aiogram.fsm.context import FSMContext

from app.kbs import cancel_ikb
from app.user.donate.donate_kbs import coin_offer_detail_ikb, coin_offers_list_ikb
from app.variables_and_funcs import is_owner
from app.crud_tables.table_users import update_coins, get_user_by_chat_id, update_starcoins
from app.crud_tables.table_users_blacklist import is_user_in_blacklist
from app.crud_tables.table_offers import (
    create_offer, update_offer_coins, update_offer_discount, get_all_offers, remove_offer_by_id, get_offer_by_id
)
from app.states import Owner
from app.lang import tr_msg

router = Router()

@router.callback_query(F.data == "get_more_coins")
async def show_offers_list(query: CallbackQuery):
    pass  # TODO: Commercial logic

@router.callback_query(lambda c: c.data.startswith("show_coin_offer_"))
async def show_coin_offer(query: CallbackQuery):
    pass  # TODO: Commercial logic

@router.callback_query(lambda c: c.data.startswith("buy_coin_offer_"))
async def buy_coin_offer_starcoins(query: CallbackQuery):
    pass  # TODO: Commercial logic

@router.callback_query(F.data == "add_coin_offer")
async def add_offer_start(query: CallbackQuery, state: FSMContext):
    pass  # TODO: Commercial logic


@router.message(Owner.waiting_for_price)
async def add_offer_price(message: Message, state: FSMContext):
    pass  # TODO: Commercial logic


@router.message(Owner.waiting_for_coins)
async def add_offer_coins(message: Message, state: FSMContext):
    pass  # TODO: Commercial logic


@router.message(Owner.waiting_for_discount)
async def add_offer_discount(message: Message, state: FSMContext):
    pass  # TODO: Commercial logic

@router.callback_query(lambda c: c.data.startswith("delete_starcoin_offer_"))
async def delete_starcoin_offer_handler(query: CallbackQuery):
    pass  # TODO: Commercial logic
