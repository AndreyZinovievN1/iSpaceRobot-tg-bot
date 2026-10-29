from aiogram import Router, F
from aiogram.types import CallbackQuery

from app.agent_of_stars.agent_panel_kbs import agent_panel_main_ikb, agent_back_ikb

router = Router()


@router.callback_query(F.data == "agent:main")
async def agent_main(query: CallbackQuery):
    pass  # TODO: Commercial logic


@router.callback_query(F.data == "agent:reports")
async def agent_reports(query: CallbackQuery):
    pass  # TODO: Commercial logic


@router.callback_query(F.data == "agent:blacklists")
async def agent_blacklists(query: CallbackQuery):
    pass  # TODO: Commercial logic


@router.callback_query(F.data == "agent:scammers")
async def agent_scammers(query: CallbackQuery):
    pass  # TODO: Commercial logic


@router.callback_query(F.data == "agent:cmds")
async def agent_cmds(query: CallbackQuery):
    pass  # TODO: Commercial logic
