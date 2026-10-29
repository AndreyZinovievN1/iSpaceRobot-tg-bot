from aiogram import Router, html
from aiogram.types import Message
from app.filters.custom_emoji import HasCustomEmoji
from app.owner.emoji_saver import TRIGGER_RE

router = Router()

@router.message(HasCustomEmoji())
async def handle_premium_emoji(message: Message, emoji_ids: list[str]):
    # Создаем список строк, где для каждого ID формируем пару: эмодзи - ID
    pass  # TODO: Commercial logic
