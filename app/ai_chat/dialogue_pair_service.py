from __future__ import annotations

import logging
import re

from app.ai_chat.corpus.learning import check_learning_text
from app.crud_tables.table_ai_chat_helpers import row_get


logger = logging.getLogger(__name__)

SYSTEM_PLACEHOLDER_RE = re.compile(
    r"^\[(?:GIF|STICKER|VOICE|MEME|MEDIA_MEME|VIDEO_NOTE_MEME|EMOJI)(?::[^\]]+)?\]",
    re.IGNORECASE,
)


def _valid_pair_text(value) -> str | None:
    pass  # TODO: Commercial logic


async def try_create_dialogue_pair(
    repo,
    *,
    chat_id: int,
    response_message_id: int | None,
    reply_to_message_id: int | None,
) -> int | None:
    pass  # TODO: Commercial logic
