import time
from app.debug.context import trace_id_var, user_id_var, chat_id_var


async def dbg_send_message(bot, *, chat_id, text, source="unknown", **kwargs):
    pass  # TODO: Commercial logic


async def dbg_send_animation(
    bot,
    *,
    chat_id,
    animation,
    caption=None,
    source="unknown",
    **kwargs
):
    pass  # TODO: Commercial logic


async def dbg_edit_message_text(
    bot,
    *,
    chat_id,
    message_id,
    text,
    source="unknown",
    **kwargs
):
    pass  # TODO: Commercial logic


async def dbg_delete_message(bot, *, chat_id, message_id, source="unknown", **kwargs):
    pass  # TODO: Commercial logic


async def dbg_get_chat_member(bot, *, chat_id, user_id, source="unknown", **kwargs):
    pass  # TODO: Commercial logic
