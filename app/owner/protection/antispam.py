from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters.command import Command
from aiogram.exceptions import TelegramBadRequest

from app.kbs import delete_ikb, clear_spamlist_100_per_ikb
from app.variables_and_funcs import (
    delete_after_delay, is_owner, is_user_in_group, is_owner_or_admin
)
from app.logs.logs import (
    log_add_user_to_spamlist, log_delete_user_from_spamlist, log_clear_spamlist
)
from app.crud_tables.table_users import update_msg_count, get_user_by_chat_id
from app.crud_tables.table_stats import update_req_count
from app.crud_tables.table_spamlist import (
    add_user_to_spamlist, is_user_in_spamlist, delete_user_from_spamlist,
    clear_spamlist
)
from config import bot
from app.db import db

router = Router()

@router.message(Command("спам", prefix="+"))
async def create_rp_cmd_handler(message: Message):
    pass  # TODO: Commercial logic

@router.message(Command("спам", prefix="-"))
async def create_rp_cmd_handler(message: Message):
    pass  # TODO: Commercial logic

@router.callback_query(F.data == "clear_spamlist")
async def create_rp_cmd_handler(query: CallbackQuery):
    pass  # TODO: Commercial logic

@router.callback_query(F.data == "yes_clear_spamlist")
async def create_rp_cmd_handler(query: CallbackQuery):
    pass  # TODO: Commercial logic

# @router.message(Command("спам", prefix="!"))
# async def create_rp_cmd_handler(message: Message):
#     await message.delete()
#     await update_req_count()
#     await update_msg_count(message.from_user.id, message.from_user.full_name, message.from_user.username)

#     if not await is_owner_or_admin(message.from_user.id):
#         msg = await message.answer(f"🚫 <a href=\"tg://user?id={message.from_user.id}\">{message.from_user.full_name}</a>, у вас отсутствует право на использования команды \"!спам\".")
#         await delete_after_delay(msg)
#         return

#     users = await db.fetch_spamlist()
#     text = f"<b>🤴🏻 Хозяин</b>: <a href=\"tg://user?id={message.from_user.id}\">{message.from_user.full_name}</a>\
#         \n<b>👤 Спам-лист пользователей:</b>"
#     for user in users:
#         user_profile = await get_user_by_chat_id(user["chat_id"])
#         text += f"\n    {f'<a href=\"tg://user?id={user['chat_id']}\">{user_profile['name'] if user_profile else 'Незнакомец'}</a>'} [<code>{user['chat_id']}</code>]"

#     await message.answer(text, reply_markup=await delete_ikb(message.from_user.id))
