from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


start_keyboards = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🔎 Wikipedia"), KeyboardButton(text="🌦️ Ob-havo")],
        [KeyboardButton(text="💸 Valyuta"), KeyboardButton(text="🌍 Tarjima")]
    ],
    resize_keyboard=True
)

location_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Lokatsiya jo'natish", request_location=True)]
    ],
    resize_keyboard=True
)