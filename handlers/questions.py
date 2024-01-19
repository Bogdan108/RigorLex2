from aiogram import Bot, Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from utils.states import Reception
from bot import bot
router = Router()


@router.message(Command(commands='consultation'))
async def fill_profile(message: Message, state: FSMContext):
    await state.set_state(Reception.name)
    await message.answer(
        "Давай начнем запись на прием, введи Фамилия, имя, отчество:",
    )


@router.message(Reception.name)
async def form_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Reception.phone_number)
    await message.answer("Отлично, теперь введи свой номер телефона:")


@router.message(Reception.phone_number)
async def form_phone_number(message: Message, state: FSMContext):
    if message.text.isdigit():
        await state.update_data(phone_number=message.text)
        await state.set_state(Reception.meeting_time)
        await message.answer(
            "Теперь давай определимся с желаемой датой и временем"
        )
    else:
        await message.answer("Введи номер, еще раз!")


@router.message(Reception.meeting_time)
async def form_meeting_time(message: Message, state: FSMContext):
    await state.update_data(meeting_time=message.text)
    await state.set_state(Reception.guest_question)
    await message.answer("Расскажи о содержании вопроса")


@router.message(Reception.guest_question)
async def guest_question(message: Message, state: FSMContext):
    if len(message.text) < 5:
        await message.answer("Введи более содержательный вопрос")
    else:
        await state.update_data(guest_question=message.text)

    data = await state.get_data()
    await state.clear()

    formatted_text = []
    [
        formatted_text.append(f"{key}: {value}")
        for key, value in data.items()
    ]
    await bot.send_message(370363468, '\n'.join(formatted_text))

@router.message()
async def handle_text(message: Message):
    await message.reply("Извините, я не понимаю эту команду.")
