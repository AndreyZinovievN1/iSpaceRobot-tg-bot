import time
from aiogram import BaseMiddleware
from .context import trace_id_var, event_name_var, user_id_var, chat_id_var


class DebugMiddleware(BaseMiddleware):
    def __init__(self, hub):
        pass  # TODO: Commercial logic

    def _extract_event_info(self, event):
        pass  # TODO: Commercial logic

    def _is_critical_error(self, error: Exception) -> bool:
        pass  # TODO: Commercial logic

    async def __call__(self, handler, event, data):
        pass  # TODO: Commercial logic
