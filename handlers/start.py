from aiogram import types
from aiogram import Dispatcher
from keyboards import start_keyboards

async def salom_ber(message: types.Message):
    await message.answer(text=f"Assalomu aleykum, xush kelibsiz! {message.from_user.full_name}", reply_markup=start_keyboards)


def register_start_handler(dp: Dispatcher):
    dp.register_message_handler(salom_ber, commands=['start'])

