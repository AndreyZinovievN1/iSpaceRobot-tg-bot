from dataclasses import dataclass


LAUGH_WORDS = [
    "ахах", "хах", "аха", "😂", "🤣", "ору", "ржу", "лол", "кек", "ору"
]

ARGUE_WORDS = [
    "бред", "чушь", "пиздишь", "неправда", "тупой", "идиот", "нахуй",
    "хуйня", "говно", "заткнись"
]

QUESTION_WORDS = [
    "?", "как", "почему", "зачем", "что делать", "куда", "где", "когда"
]


@dataclass
class SpaceMood:
    name: str
    laugh_score: int
    argue_score: int
    question_score: int
    messages_count: int


def count_words(text: str, words: list[str]) -> int:
    pass  # TODO: Commercial logic


def detect_mood(messages: list[str]) -> SpaceMood:
    pass  # TODO: Commercial logic
