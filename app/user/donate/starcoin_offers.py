from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery, LabeledPrice, PreCheckoutQuery
import re
from aiogram.fsm.context import FSMContext

from app.kbs import cancel_ikb
from app.user.donate.donate_kbs import starcoin_offer_detail_ikb, starcoin_offers_list_ikb
from app.variables_and_funcs import is_owner
from app.crud_tables.table_users import update_starcoins
from app.crud_tables.table_users_blacklist import is_user_in_blacklist
from app.crud_tables.table_offers import (
    create_starcoins_offer, update_starcoins_offer_amount, update_starcoins_offer_discount,
    get_all_starcoins_offers, get_starcoins_offer_by_id, remove_starcoins_offer_by_id
)
from app.crud_tables.table_log_group import get_log_group_id
from app.states import Owner
from app.lang import tr_msg

router = Router()


async def _safe_edit_or_resend(query: CallbackQuery, text: str, reply_markup=None):
    pass  # TODO: Commercial logic


@router.callback_query(F.data == "get_more_starcoins")
async def show_offers_list(query: CallbackQuery):
    pass  # TODO: Commercial logic


@router.callback_query(lambda c: c.data.startswith("show_starcoin_offer_"))
async def show_starcoin_offer(query: CallbackQuery):
    pass  # TODO: Commercial logic


@router.callback_query(lambda c: c.data.startswith("buy_starcoins_offer_"))
async def buy_coin_offer(query: CallbackQuery):
    pass  # TODO: Commercial logic


async def send_stars_invoice(query: CallbackQuery, offer: dict, offer_id: int):
    pass  # TODO: Commercial logic


@router.pre_checkout_query()
async def pre_checkout_handler(pre_checkout_query: PreCheckoutQuery):
    pass  # TODO: Commercial logic


@router.message(F.successful_payment)
async def process_successful_payment(message: Message, bot: Bot):
    pass  # TODO: Commercial logic


@router.callback_query(F.data == "add_starcoin_offer")
async def add_offer_start(query: CallbackQuery, state: FSMContext):
    pass  # TODO: Commercial logic


@router.message(Owner.waiting_for_price_for_starcoins)
async def add_offer_price(message: Message, state: FSMContext):
    pass  # TODO: Commercial logic


@router.message(Owner.waiting_for_starcoins)
async def add_offer_starcoins(message: Message, state: FSMContext):
    pass  # TODO: Commercial logic


@router.message(Owner.waiting_for_discount_for_starcoins)
async def add_offer_discount(message: Message, state: FSMContext):
    pass  # TODO: Commercial logic


@router.callback_query(lambda c: c.data.startswith("delete_starcoin_offer_"))
async def delete_starcoin_offer_handler(query: CallbackQuery):
    pass  # TODO: Commercial logic
