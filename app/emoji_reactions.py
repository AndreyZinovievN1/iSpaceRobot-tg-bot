from aiogram import Router, F
from aiogram.types import (
    ReactionCount
)
import re
from datetime import datetime, timedelta
from pytz import timezone
from asyncio import sleep
from random import choice

from config import bot

emoji_reactions_router = Router()

@emoji_reactions_router.raw_event(types=ReactionCount)
async def reaction_handler(event: ReactionCount):
    pass  # TODO: Commercial logic
