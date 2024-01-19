from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.filters import Command
from lexicon.lexicon import LEXICON_RU

# Инициализируем роутер уровня модуля
router = Router()

# Этот хэндлер будет срабатывать на команду "/services"
@router.message(Command(commands='services'))
async def process_command_start(message: Message):
    await message.answer(text=LEXICON_RU['services'])

# Этот хэндлер будет срабатывать на команду "/help"
@router.message(Command(commands='help'))
async def process_command_start(message: Message):
    await message.answer(text=LEXICON_RU['help'])

# Этот хэндлер будет срабатывать на команду "/consultation"
#@router.message(Command(commands='consultation'))
#async def process_command_start(message: Message):
#    await message.answer(text=LEXICON_RU['consultation'])

    # Этот хэндлер будет срабатывать на команду "/services"
@router.message(Command(commands='contacts'))
async def process_command_start(message: Message):
    await message.answer(text=LEXICON_RU['contacts'])

    # Этот хэндлер будет срабатывать на команду "/support"
@router.message(Command(commands='support'))
async def process_command_start(message: Message):
    await message.answer(text=LEXICON_RU['consultation'])
