from aiogram import Router
from aiogram.types import Message
from ...lang import tr_msg

from ...variables_and_funcs import (
    delete_after_delay, format_marriage_info, is_owner_or_admin
)
from ...kbs import create_navigation_keyboard_for_spamlist
from ...crud_tables.table_users import (
    get_user_by_chat_id, update_msg_count
)
from ...crud_tables.table_stats import update_req_count
from ...crud_tables.table_settings import get_settings_by_group_id
from ...crud_tables.table_users_blacklist import is_user_in_blacklist
from ...db import db 
from ...weddings_divorces import get_marriage  
from config import bot
from .nav import (
    create_navigation_keyboard, POSITIONS_PER_PAGE, MARRIAGES_PER_PAGE,
    get_groups_top_page, get_marriages_top_page, get_spamlist_page, cache_banana, cache_coins, cache_msg,
    fetch_users_for_top
)

router = Router()


@router.message(lambda message: message.text == "Топ банан")
async def top_banana(message: Message):
    # Эти функции (update_req_count и т.д.) должны быть импортированы из вашего модуля статистики
    # await update_req_count() 
    # await update_msg_count(message.from_user.id, message.from_user.full_name, message.from_user.username)
    pass  # TODO: Commercial logic

@router.message(lambda message: message.text == "Топ монет")
async def top_coins_text(message: Message):
    pass  # TODO: Commercial logic

@router.message(lambda message: message.text == "Топ смс")
async def top_msg_text(message: Message):
    pass  # TODO: Commercial logic

@router.message(lambda message: message.text == "Топ")
async def top_message(message: Message):
    pass  # TODO: Commercial logic

@router.message(lambda message: message.text == "Браки") 
async def top_message(message: Message):
    pass  # TODO: Commercial logic
    
# @router.message(lambda message: message.text == "Гифки") 
# async def top_message(message: Message):
#     await update_req_count()

#     await message.answer_animation(
#         "CgACAgQAAxkBAAICaGfJwC0Uu2D3UrEIexWoYYdM0fYZAAJsCgACfBRQUFb_U-ZVPi2gNgQ",
#         caption="CgACAgQAAxkBAAICaGfJwC0Uu2D3UrEIexWoYYdM0fYZAAJsCgACfBRQUFb_U-ZVPi2gNgQ",
#         reply_markup=await create_gifs_navigation_keyboard(0, 1, message.from_user.id)
#     )
    
    # user = await get_user_by_chat_id(message.from_user.id)

    # if await is_user_in_blacklist(message.from_user.id):
    #     await bot.send_message(
    #         message.from_user.id, "Вы находитесь в черном списке. Я с вами не разговариваю!"
    #     )
    #     return

    # text = ""
    # now = datetime.now(timezone('Europe/Moscow'))
    # gifs = await db.fetch_catalog_gifs()
    # if gifs:
    #     for gif in gifs[:5]:
    #         text += f"\n\n<code>{gif['gif_id']}</code>"

    # total_pages = (len(gifs) + MARRIAGES_PER_PAGE - 1) // MARRIAGES_PER_PAGE

    # await message.delete()
    # await message.answer(
    #     f"<a href=\"tg://user?id={message.from_user.id}\">{message.from_user.full_name}</a>\n"
    #     f"🗃 Всего GIF: {len(gifs)}\n\n"
    #     f"🖼 Список всех GIF:"
    #     f"{text}",
    #     reply_markup=await create_navigation_keyboard(0, total_pages, message.from_user.id, "top_marriages"),
    #     disable_web_page_preview=True
    # )

@router.message(lambda message: message.text == "!спам")
async def top_banana(message: Message):
    pass  # TODO: Commercial logic
