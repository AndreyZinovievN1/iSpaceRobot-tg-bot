from aiogram import Router, F
from aiogram.types import (
    Message, CallbackQuery
)
from aiogram.filters.command import Command
import re
from datetime import datetime, timedelta
from random import randint, choice
from asyncio import sleep
from pytz import timezone
from bs4 import BeautifulSoup

from ..kbs import  bags_ikb
from ..variables_and_funcs import (
    delete_after_delay
)
from ..crud_tables.table_users import (
    get_user_by_chat_id
)
from ..crud_tables.table_users_blacklist import is_user_in_blacklist
from config import bot

coin_offers_router = Router()

@coin_offers_router.callback_query(lambda c: c.data.startswith("get_more_coins"))
async def random_bag(query: CallbackQuery):
    pass  # TODO: Commercial logic
