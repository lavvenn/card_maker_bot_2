from aiogram.fsm.state import State, StatesGroup


class Registration(StatesGroup):

    lastname = State()
    firstname = State()

    group = State()

    photo = State()

    confirming = State()
