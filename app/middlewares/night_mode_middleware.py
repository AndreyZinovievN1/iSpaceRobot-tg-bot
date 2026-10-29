from typing import Callable, Dict, Any, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import Message
from app.crud_tables.table_night_mode import (
    get_night_mode_by_group_id, add_night_mode 
)
from app.variables_and_funcs import is_now_night, is_owner_or_chat_admin

class NightModeMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any]
    ) -> Any:
        # Работаем только в группах
        pass  # TODO: Commercial logic
