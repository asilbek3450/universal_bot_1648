from aiogram import types
from aiogram import Dispatcher
from config import OBHAVO_KEY
from keyboards import location_kb
# url = f'https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&exclude=hourly,daily&appid={OBHAVO_KEY}'

async def ob_havo_handler(message: types.Message):
    await message.answer(text="Siz ob-havo bo'limiga kirdingiz, obhavoni bilish uchun lokatsiya jo'nating", reply_markup=location_kb)


def register_obhavo_handler(dp: Dispatcher):
    dp.register_message_handler(ob_havo_handler, text="🌦️ Ob-havo")

