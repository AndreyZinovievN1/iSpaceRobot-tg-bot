from aiogram.filters import BaseFilter
from aiogram.types import Message

class HasCustomEmoji(BaseFilter):
    async def __call__(self, message: Message) -> bool | dict:
        pass  # TODO: Commercial logic
