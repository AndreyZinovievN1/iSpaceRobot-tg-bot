from aiogram.types import Message

from app.ai_chat.space_agent import diagnose_space_agent, run_space_agent


async def try_markov_reply(
    message: Message,
    db,
    *,
    force: bool = False,
    save_message: bool = True,
) -> bool:
    pass  # TODO: Commercial logic


async def diagnose_markov_reply(
    message: Message,
    db,
    *,
    force: bool = False,
):
    pass  # TODO: Commercial logic
