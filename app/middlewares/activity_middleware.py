from typing import Callable, Awaitable, Dict, Any

from aiogram import BaseMiddleware
from aiogram.types import Message

from app.crud_tables.table_activity import log_activity
from app.crud_tables.table_profile_history import (
    add_user_name_history,
    add_user_seen_chat,
)
from config import logger


class ActivityMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any],
    ) -> Any:

        pass  # TODO: Commercial logic
