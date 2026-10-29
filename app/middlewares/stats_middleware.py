from aiogram import BaseMiddleware
from aiogram.types import Message
from typing import Callable, Dict, Any, Awaitable

from ..crud_tables.table_users import update_msg_count
from ..crud_tables.table_settings import update_msg_count_for_group

class StatsMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any]
    ) -> Any:
        # 1. Логика учета (выносим из твоего group_filter)
        user = event.from_user
        if user:
            # Твои функции обновления БД (делаем асинхронно)
            await update_msg_count(
                chat_id=user.id, 
                name=user.full_name, 
                username=user.username, 
                message=event
            )
            await update_msg_count_for_group(event.chat.id)

        # 2. Пробрасываем сообщение дальше к следующему Middleware или Хендлеру
        return await handler(event, data)