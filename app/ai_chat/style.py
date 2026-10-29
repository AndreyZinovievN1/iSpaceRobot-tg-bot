import random

from app.ai_chat.filters import normalize_phrase


PREFIXES = [
    "фиксирую: ",
    "по космическим меркам, ",
    "моя орбита подсказывает: ",
]

FUNNY_ENDINGS = [
    " и это уже похоже на локальную аномалию",
    " чат официально теряет орбиту",
]

QUESTION_ENDINGS = [
    " но это точно нуждается в расследовании",
    " я бы занес это в архив странностей",
]


def apply_space_style(phrase: str, *, mood_name: str, reason: str) -> str | None:
    pass  # TODO: Commercial logic
