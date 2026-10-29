from __future__ import annotations


HUMAN_NSFW_LABELS = frozenset(
    {"safe", "porn", "hentai", "borderline", "unusable"}
)


class AIChatNSFWHumanLabelsTable:
    def __init__(self, db):
        pass  # TODO: Commercial logic

    async def set_label(
        self,
        *,
        alert_id: int,
        human_label: str,
        labeled_by_user_id: int,
    ):
        pass  # TODO: Commercial logic

    async def fetch_label_for_alert(self, *, alert_id: int):
        pass  # TODO: Commercial logic

    async def fetch_current_labels(self):
        pass  # TODO: Commercial logic
