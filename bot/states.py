from aiogram.fsm.state import StatesGroup, State


class CurrentState(StatesGroup):
    entering_quantity_item = State()
    check_payment = State()
