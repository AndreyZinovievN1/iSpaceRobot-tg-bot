import re
from datetime import datetime, timedelta
from pytz import timezone
from typing import Optional, Union
from asyncio import sleep
from dateutil.relativedelta import relativedelta
from dateutil.parser import isoparse
from apscheduler.triggers.date import DateTrigger
from random import choice
from aiogram.exceptions import TelegramBadRequest

from .db import db
from .crud_tables.table_users import get_user_by_chat_id
from .crud_tables.table_admins import get_admin_by_chat
from .crud_tables.table_channels_to_control import update_channels_to_control
from .crud_tables.table_night_mode import get_night_mode_by_group_id
from config import bot, scheduler
from .lang import tr_chat

LOCALES = {
    "ru": {
        "user_choose": "<b>Язык для себя</b>\nВыберите язык:",
        "user_ok": "✅ Ваш язык установлен: {name}",
        "chat_choose": "<b>Язык для чата</b>\nВыберите язык:",
        "chat_ok": "✅ Язык чата установлен: {name}",
        "only_admins": "Только владелец/админ чата может менять язык чата.",
    },
    "ua": {
        "user_choose": "<b>Мова для себе</b>\nОберіть мову:",
        "user_ok": "✅ Вашу мову встановлено: {name}",
        "chat_choose": "<b>Мова для чату</b>\nОберіть мову:",
        "chat_ok": "✅ Мову чату встановлено: {name}",
        "only_admins": "Лише власник/адмін чату може змінювати мову чату.",
    },
    "en": {
        "user_choose": "<b>Your language</b>\nChoose a language:",
        "user_ok": "✅ Your language set to: {name}",
        "chat_choose": "<b>Chat language</b>\nChoose a language:",
        "chat_ok": "✅ Chat language set to: {name}",
        "only_admins": "Only chat owner/admin can change the chat language.",
    },
}

LANG_NAMES = {"ru": "Русский", "ua": "Українська", "en": "English"}


def t(lang: str, key: str) -> str:
    pass  # TODO: Commercial logic


WELCOME_TEXT = "texts.welcome"

async def trf(chat_id: int, key: str, **kwargs) -> str:
    pass  # TODO: Commercial logic


def is_now_night(start_t, end_t, tz_name):
    """Проверяет, наступила ли ночь по часовому поясу чата"""
    pass  # TODO: Commercial logic


TUTORIAL_TO_ADD_GRP_CMD = "tutorials.add_grp_cmd"

systemmsg_info = "infos.systemmsg"
antiarab_info = "infos.antiarab"
antibot_info = "infos.antibot"
antichannel_info = "infos.antichannel"
antiforward_info = "infos.antiforward"
antilink_info = "infos.antilink"
antihyper_info = "infos.antihyper"
antibutton_info = "infos.antibutton"
antiuser_info = "infos.antiuser"
antispam_info = "infos.antispam"
shalosti_info = "infos.shalosti"
wedding_info = "infos.wedding"
roulette_info = "infos.roulette"

reaction_to_owner_pins = "reactions.to_owner_pins"
reaction_to_pin = "reactions.to_pin"
reaction_to_pin_in_night = "reactions.to_pin_night"


async def get_reaction(chat_id: int, key: Union[str, tuple, list]) -> Optional[str]:
    pass  # TODO: Commercial logic


WELCOME_TEXT = """@iSpaceRobot — ваш страж порядка!

👮 Следит за атмосферой и модерирует чат.
🎲 Развлечения и игры для весёлого времяпрепровождения.
⚙️ Гибкие настройки для удобства администраторов.
🔒 Защита от спама и нежелательных сообщений.

📌 /help — для полного списка команд.

🔗 <a href=\"https://t.me/catalog_iSpace\">Каталог ✨</a>
"""

TUTORIAL_TO_ADD_RP_CMD = """
Неправильное написание команды!
Пример:
Строка: <code>+рп !мяу name1 &lt;b&gt;<b>помяукал</b>&lt;/b&gt; для name2 😽. CgACAgIAAxkBAAOAZ4YEcZjoBwgQr3QywDw7AdU0oBEAAtITAAKgPVFISFHfCljqCI82BA</code>
Команда: !мяу
Текст: name1 <b>помяукал</b> для name2.
ID гифки: CgACAgIAAxkBAAOAZ4YEcZjoBwgQr3QywDw7AdU0oBEAAtITAAKgPVFISFHfCljqCI82BA
"""

TUTORIAL_TO_ADD_GRP_CMD = """
Неправильное написание команды!
Пример:
Строка: <code>+грп !мяу name1 &lt;b&gt;<b>помяукал</b>&lt;/b&gt; для name2 😽. CgACAgIAAxkBAAOAZ4YEcZjoBwgQr3QywDw7AdU0oBEAAtITAAKgPVFISFHfCljqCI82BA</code>
Команда: !мяу
Текст: name1 <b>помяукал</b> для name2.
ID гифки: CgACAgIAAxkBAAOAZ4YEcZjoBwgQr3QywDw7AdU0oBEAAtITAAKgPVFISFHfCljqCI82BA
"""

systemmsg_info = "🔧 Системные - удаляет системные сообщения (вступления/добавления/выходы/удаления) участников."
antiarab_info = "👳🏾‍♂️ Арабский - удаляет арабские буквы и даёт бан (в том числе за подобные имена и/или био)."
antibot_info = "🤖 Боты - даёт бан новым ботам, а тем кто их добавляет мут на 10 минут."
antichannel_info = "👤 Каналы - удаляет сообщения пользователей пишущих от имени канала и блокирует возможность писать так в дальнейшем."
antiforward_info = "📢 Пересылки - удаляет и даёт мут на 5 минут за пересылку из каналов (кроме привязанного к данной группе)."
antilink_info = "🔗 Ссылки - удаляет и даёт мут на 5 минут за ссылки (не относящиеся к данной группе)."
antihyper_info = "🔍 Гиперссылки - удаляет и даёт мут на 5 минут за гиперссылки."
antibutton_info = "🖲️ Кнопки - удаляет и даёт мут на 5 минут за ссылки в кнопках."
antiuser_info = "🌀 @Юзеры - удаляет и даёт мут на 10 минут за @юзеры (каналов/групп/ботов)."
antispam_info = "🛡️ Антиспам - удаляет и выдаёт бан за спам (одинаковые сообщения, флуд и т.п.)."

reaction_to_owner_pins = (
    'Ты как бог пинов, владеешь ими лучше всех! 👑📌',
    'Каждый твой пин — это произведение искусства! 🎨📌',
    'С такими пинами, как у тебя, этот чат не может не быть на высоте! 🔥📌',
    'Твои пины — это просто шедевры, никто не сравнится! 🏆📌',
    'Каждый пин от тебя — это как новый закон! 📜📌',
    'Пинить, как ты, могут только истинные мастера! 💥📌',
    'Никто не делает пины так эффектно, как ты! 🌟📌',
    'Ты знаешь, как сделать пины эпичными! Каждое сообщение становится легендой! 🔥📌',
    'Ты как стратег, управляешь пинами как истинный командир! ⚔️📌',
    'Пин — твой главный инструмент власти в этом чате! 🛠️📌',
    'Твои пины всегда попадают в цель, как стрелы Амура! 💘📌',
    'Ты — тот, кто делает пины важными! Без тебя они бы не имели такого значения! 🌟📌',
    'Ты заслуживаешь награды за лучшую стратегию пинов! 🏅📌',
    'Если бы пины были олимпийским видом спорта, ты был бы чемпионом! 🥇📌',
    'Твой каждый пин — как поворотная точка в истории чата! 🔄📌',
    'Пинить — это искусство, и ты — великий художник! 🎨📌',
    'В этом чате твой пин — это как последний аккорд симфонии! 🎶📌',
    'Все пины — как исторические вехи в этом чате, и ты их пишешь! 📚📌'
)

reaction_to_pin = (
    'Блин, кто ему дал админку?',
    'Ради бога, заберите у этого человека право на закреп!',
    'Хватит!',
    'И что это?',
    'Господи кто этому человеку дал право на закреп?',
    'Пина-дрочер!!!',
    '...',
    'Столько шума, а напрасно, не кто все равно это не будет смотреть!',
    'Он не устал пинить?',
    'Прекрати пинить всякую хрень -_-',
    'Всем пофигу -.-',
    'Делать нечего?',
    'Попу свою запинь',
    'Все равно не кому это не интересно.',
    'Да что ты что говоришь сказочник :)',
    'Бла бла бла...'
)

reaction_to_pin_in_night = (
    'Уффф',
    'Все спят!',
    'Дай поспать!',
    'Может хватит уже действительно?',
    'Ааааааа зачем с уведомлением?',
    'Я только задремал, а тебе надо было сейчас это крипить('
)

timezones = [
    "Europe/Moscow",
    "Europe/Kaliningrad",
    "Europe/Samara",
    "Asia/Yekaterinburg",
    "Asia/Omsk",
    "Asia/Novosibirsk",
    "Asia/Krasnoyarsk",
    "Asia/Irkutsk",
    "Asia/Yakutsk",
    "Asia/Vladivostok",
    "Asia/Sakhalin",
    "Asia/Magadan",
    "Asia/Kamchatka",
    "Europe/Minsk",
    "Europe/Kyiv",
    "Asia/Almaty",
    "Asia/Aqtobe",
    "Asia/Atyrau",
    "Asia/Oral",
    "Asia/Qostanay",
    "Asia/Qyzylorda",
    "Asia/Aqtau",
    "Asia/Tashkent",
    "Asia/Bishkek",
    "Asia/Dushanbe",
    "Asia/Ashgabat",
    "Asia/Yerevan",
    "Asia/Tbilisi",
    "Asia/Baku",
    "Asia/Jerusalem",
    "Europe/Istanbul",
    "Europe/Chisinau"
]

CLOSE_PEOPLE = """
Теплый зал, несколько близких людей, тихие поздравления. Свидетели улыбаются, наблюдая за обменом кольцами. Регистратор объявляет их супругами, и в воздухе раздается мягкий аплодисмент. Они обнимаются, чувствуя тепло и поддержку тех, кто пришел разделить этот момент. 🥂
"""

WITH_GUESTS = """
Гул голосов затихает, когда жених и невеста говорят заветное "да". Аплодисменты сотрясают зал, кто-то запускает конфетти, звучит музыка. Друзья и родные с радостью бросаются поздравлять, тосты звучат один за другим. Свадьба разгорается ярким праздником, где любовь – главный герой. 🎶💍
"""


EXPECTED_DELETE_ERRORS = (
    "message to delete not found",
    "message can't be deleted",
)


async def delete_after_delay(msg, delay=10):
    pass  # TODO: Commercial logic


async def welcome_text():
    pass  # TODO: Commercial logic


telegram_languages = {
    "en": "English",
    "ru": "Русский",
    "uk": "Українська",
    "be": "Беларуская",
    "es": "Español",
    "de": "Deutsch",
    "it": "Italiano",
    "pt-br": "Português Brasileiro",
    "fr": "Français",
    "id": "Bahasa Indonesia",
    "ar": "العربية",
    "fa": "فارسی",
    "ko": "한국어",
    "tr": "Türkçe",
    "ja": "日本語",
    "zh-hans": "简体中文",
    "zh-hant": "繁體中文",
    "hi": "हिन्दी",
    "pl": "Polski",
    "uz": "Oʻzbekcha",
    "he": "עברית",
    "bg": "Български",
    "ro": "Română",
    "kk": "Қазақша"
}


async def bot_can_delete_messages(message) -> bool:
    pass  # TODO: Commercial logic


async def is_owner(chat_id):
    pass  # TODO: Commercial logic


async def is_admin(chat_id):
    pass  # TODO: Commercial logic


async def is_chat_admin(group_id, chat_id):
    pass  # TODO: Commercial logic


async def is_chat_creator(group_id, user_id):
    pass  # TODO: Commercial logic


async def get_chat_creator(channel_id):
    pass  # TODO: Commercial logic


async def is_owner_or_chat_admin(group_id, chat_id):
    pass  # TODO: Commercial logic


async def is_owner_or_admin(chat_id):
    pass  # TODO: Commercial logic


async def is_user_in_group(group_id, user_id):
    pass  # TODO: Commercial logic


async def get_group_owner(chat_id: int):
    pass  # TODO: Commercial logic


def get_next_run_time(target_time, tz_name):
    pass  # TODO: Commercial logic


async def turn_on_night_mode(chat_id: int):
    pass  # TODO: Commercial logic


async def turn_off_night_mode(chat_id: int):
    pass  # TODO: Commercial logic


async def apply_replacements(text: str, message) -> str:
    pass  # TODO: Commercial logic


async def check_channel_subs():
    pass  # TODO: Commercial logic


def parse_time(time_string: Optional[str]) -> Optional[datetime]:
    pass  # TODO: Commercial logic


async def format_marriage_info(marriage):
    pass  # TODO: Commercial logic
