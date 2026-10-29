from __future__ import annotations


class AIChatDialoguePairsTable:
    def __init__(self, db):
        pass  # TODO: Commercial logic

    async def fetch_candidate_for_response(
        self,
        chat_id: int,
        response_message_id: int,
    ):
        pass  # TODO: Commercial logic

    async def insert_dialogue_pair(
        self,
        *,
        chat_id: int,
        source_message_id: int,
        response_message_id: int,
        source_text: str,
        response_text: str,
        source_user_id: int | None,
        response_user_id: int | None,
        message_thread_id: int | None,
        response_role: str,
    ) -> int | None:
        pass  # TODO: Commercial logic

    async def fetch_similar_dialogue_pairs(
        self,
        *,
        chat_id: int,
        source_text: str,
        message_thread_id: int | None = None,
        exclude_response_message_id: int | None = None,
        limit: int = 10,
    ):
        pass  # TODO: Commercial logic
