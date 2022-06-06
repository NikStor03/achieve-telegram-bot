from aiogram.dispatcher.filters.state import State, StatesGroup


class CreateAchieve(StatesGroup):

    name = State()
    end_day = State()
    total_aim = State()
    daily_aim = State()
    short_name = State()