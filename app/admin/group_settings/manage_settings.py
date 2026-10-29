from aiogram import Router, F
from aiogram.types import CallbackQuery

from ...kbs import settings_ikb, shalosti_ikb, chat_lang_menu_ikb
from ...variables_and_funcs import (
    is_admin, is_owner_or_chat_admin, systemmsg_info, antiarab_info, antibot_info, antichannel_info, 
    antiforward_info, antilink_info, antihyper_info, antibutton_info, antiuser_info, antispam_info, shalosti_info, wedding_info, roulette_info, t, is_chat_creator
)
from ...crud_tables.table_settings import (
    add_settings, update_settings, get_settings_by_group_id, update_chat_lang
)

from ...i18n import t
from ...lang import tr_chat

router = Router()

@router.callback_query(F.data == "chat_lang_open")
async def chat_lang_open(cb: CallbackQuery):
    pass  # TODO: Commercial logic

@router.callback_query(F.data.startswith("lang:set:chat:"))
async def chat_lang_set(cb: CallbackQuery):
    pass  # TODO: Commercial logic

@router.callback_query(F.data == "settings")
async def settings(query: CallbackQuery):
    pass  # TODO: Commercial logic

@router.callback_query(F.data == "systemmsg_info")
async def settings(query: CallbackQuery):
    pass  # TODO: Commercial logic

@router.callback_query(F.data == "systemmsg")
async def settings(query: CallbackQuery):
    pass  # TODO: Commercial logic

@router.callback_query(F.data == "antiarab_info")
async def settings(query: CallbackQuery):
    pass  # TODO: Commercial logic

@router.callback_query(F.data == "antiarab")
async def settings(query: CallbackQuery):
    pass  # TODO: Commercial logic

@router.callback_query(F.data == "antibot_info")
async def settings(query: CallbackQuery):
    pass  # TODO: Commercial logic

@router.callback_query(F.data == "antibot")
async def settings(query: CallbackQuery):
    pass  # TODO: Commercial logic

@router.callback_query(F.data == "antichannel_info")
async def settings(query: CallbackQuery):
    pass  # TODO: Commercial logic

@router.callback_query(F.data == "antichannel")
async def settings(query: CallbackQuery):
    pass  # TODO: Commercial logic

@router.callback_query(F.data == "antiforward_info")
async def settings(query: CallbackQuery):
    pass  # TODO: Commercial logic

@router.callback_query(F.data == "antiforward")
async def settings(query: CallbackQuery):
    pass  # TODO: Commercial logic

@router.callback_query(F.data == "antilink_info")
async def settings(query: CallbackQuery):
    pass  # TODO: Commercial logic

@router.callback_query(F.data == "antilink")
async def settings(query: CallbackQuery):
    pass  # TODO: Commercial logic

@router.callback_query(F.data == "antihyper_info")
async def settings(query: CallbackQuery):
    pass  # TODO: Commercial logic

@router.callback_query(F.data == "antihyper")
async def settings(query: CallbackQuery):
    pass  # TODO: Commercial logic

@router.callback_query(F.data == "antibutton_info")
async def settings(query: CallbackQuery):
    pass  # TODO: Commercial logic

@router.callback_query(F.data == "antibutton")
async def settings(query: CallbackQuery):
    pass  # TODO: Commercial logic

@router.callback_query(F.data == "antiuser_info")
async def settings(query: CallbackQuery):
    pass  # TODO: Commercial logic

@router.callback_query(F.data == "antiuser")
async def settings(query: CallbackQuery):
    pass  # TODO: Commercial logic

@router.callback_query(F.data == "antispam_info")
async def settings(query: CallbackQuery):
    pass  # TODO: Commercial logic

@router.callback_query(F.data == "antispam_switch")
async def settings(query: CallbackQuery):
    pass  # TODO: Commercial logic

@router.callback_query(F.data == "shalosti_info")
async def settings(query: CallbackQuery):
    pass  # TODO: Commercial logic


@router.callback_query(F.data == "shalosti_page")
async def settings(query: CallbackQuery):
    pass  # TODO: Commercial logic


@router.callback_query(F.data == "nsfw_info")
async def settings(query: CallbackQuery):
    pass  # TODO: Commercial logic


@router.callback_query(F.data == "nsfw_switch")
async def settings(query: CallbackQuery):
    pass  # TODO: Commercial logic

@router.callback_query(F.data == "wedding_info")
async def settings(query: CallbackQuery):
    pass  # TODO: Commercial logic


@router.callback_query(F.data == "wedding_switch")
async def settings(query: CallbackQuery):
    pass  # TODO: Commercial logic

@router.callback_query(F.data == "roulette_info")
async def settings(query: CallbackQuery):
    pass  # TODO: Commercial logic

@router.callback_query(F.data == "roulette_switch")
async def settings(query: CallbackQuery):
    pass  # TODO: Commercial logic
