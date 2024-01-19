import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from config_data.config import Config, load_config
from handlers import main_handler, questions

# Функция конфигурирования и запуска бота
async def main(bot:Bot, dp:Dispatcher):

    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    # Загружаем конфиг в переменную config
    config: Config = load_config()

    # Инициализируем бот и диспетчер
    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher()

    # Регистриуем роутеры в диспетчере
    dp.include_routers(main_handler.router, questions.router)

    asyncio.run(main(bot, dp))