from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from app.crud_tables.table_subs import get_all_subscriptions
from app.crud_tables.table_owner import get_admin_mode
from app.variables_and_funcs import is_owner
from app.lang import tr_chat


CHART_CATEGORY_TITLES = {
    "anime": "🎌 Аниме",
    "flags": "🌍 Флаги",
    "cats": "🐱 Котики",
    "games": "🎮 Игры",
    "space": "🌌 Космос",
    "memes": "😂 Мемы",
    "other": "🎨 Разное",
}


def coin_offers_list_ikb(offers: list, exclude_id: int | None = None, is_owner: bool = False):
    pass  # TODO: Commercial logic


def coin_offer_detail_ikb(offer_id: int, offers: list, is_owner: bool = False):
    pass  # TODO: Commercial logic


def starcoin_offers_list_ikb(offers: list, exclude_id: int | None = None, is_owner: bool = False):
    pass  # TODO: Commercial logic


def starcoin_offer_detail_ikb(offer_id: int, offers: list, is_owner: bool = False):
    pass  # TODO: Commercial logic


async def donate_ikb(user_id: int, page: int = 1):
    pass  # TODO: Commercial logic


async def chart_categories_ikb(user_id: int):
    pass  # TODO: Commercial logic


async def choose_vip_plan_ikb(user_id: int):
    pass  # TODO: Commercial logic


async def subs_admin_ikb():
    pass  # TODO: Commercial logic


async def transactions_delete_ikb(user_id):
    pass  # TODO: Commercial logic


async def choose_currency_exchange_ikb(user_id):
    pass  # TODO: Commercial logic


async def choose_currency_transfer_ikb(user_id):
    pass  # TODO: Commercial logic


async def confirm_currency_action_ikb(user_id):
    pass  # TODO: Commercial logic


async def transactions_delete_ikb(user_id: int, page: int = 1, total_pages: int = 1):
    pass  # TODO: Commercial logic
