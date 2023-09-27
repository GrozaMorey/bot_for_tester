from aiogram.dispatcher.filters.state import State, StatesGroup


class EditBadge(StatesGroup):
    waiting_for_number_badge = State()