from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.utils.keyboard import InlineKeyboardBuilder


from ..crud_tables.table_log_group import get_log_group_id

router = Router()

class ReportState(StatesGroup):
    description = State()
    photo = State()
    target_nickname = State()
    target_id = State()
    target_username = State()

@router.message(Command("report"))
async def start_report(message: types.Message, state: FSMContext):
    pass  # TODO: Commercial logic

@router.message(ReportState.description)
async def process_description(message: types.Message, state: FSMContext):
    pass  # TODO: Commercial logic

@router.message(ReportState.photo, F.photo)
async def process_photo(message: types.Message, state: FSMContext):
    # Берем самое качественное фото (последнее в списке)
    pass  # TODO: Commercial logic

@router.message(ReportState.target_nickname)
async def process_nickname(message: types.Message, state: FSMContext):
    pass  # TODO: Commercial logic

@router.callback_query(ReportState.target_id, F.data == "skip_id")
@router.message(ReportState.target_id)
async def process_id(event: types.Message | types.CallbackQuery, state: FSMContext):
    pass  # TODO: Commercial logic

@router.callback_query(ReportState.target_username, F.data == "skip_username")
@router.message(ReportState.target_username)
async def finish_report(event: types.Message | types.CallbackQuery, state: FSMContext):
    pass  # TODO: Commercial logic
