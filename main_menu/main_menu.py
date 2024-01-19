from aiogram.types import BotCommand

main_menu_commands = [
        BotCommand(command='/services',
                   description='Наши услуги'),
        BotCommand(command='/consultation',
                   description='Консультация'),
        BotCommand(command='/contacts',
                   description='О нас'),
        BotCommand(command='/support',
                   description='Поддержка'),
        BotCommand(command='/help',
                   description='Информация по работе бота')
    ]