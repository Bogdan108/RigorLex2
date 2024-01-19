from aiogram.fsm.state import StatesGroup, State

class Reception(StatesGroup):
    name = State()
    phone_number = State()
    meeting_time = State()
    guest_question = State()
