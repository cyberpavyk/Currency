from aiogram.fsm.state import State, StatesGroup

class Calc(StatesGroup):
    id = State()
    input = State()
