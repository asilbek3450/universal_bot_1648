import logging
from aiogram import Bot, Dispatcher, executor, types
from config import API_TOKEN
from handlers.start import register_start_handler
from handlers.obhavo import register_obhavo_handler

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot=bot)

register_start_handler(dp=dp)
register_obhavo_handler(dp=dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

