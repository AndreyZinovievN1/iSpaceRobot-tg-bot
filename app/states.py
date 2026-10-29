from aiogram.fsm.state import State, StatesGroup

class User(StatesGroup):
    bet_on_duel = State()

    coins_exchange_amount = State()
    starcoins_exchange_amount = State()
    
    coins_transfer_amount = State()
    starcoins_transfer_amount = State()

class ChatOwner(StatesGroup):
    log_group_id = State()

    count_of_active_users_for_kick = State()
    count_of_inactive_users_for_kick = State()

    welcome_text = State()

class Owner(StatesGroup):
    welcome_text = State()

    daily_coins_transfer_limit = State()
    daily_starcoins_transfer_limit = State()

    waiting_for_price = State()
    waiting_for_coins = State()
    waiting_for_discount = State()

    waiting_for_price_for_starcoins = State()
    waiting_for_starcoins = State()
    waiting_for_discount_for_starcoins = State()

    waiting_for_divorce_price = State()

    waiting_for_price_per_user = State()

class BizAiSetupState(StatesGroup):
    waiting_for_description = State()

class ShopAdmin(StatesGroup):
    waiting_for_text_m = State()
    waiting_for_text_f = State()
    waiting_for_price = State()
    confirm_delete = State()