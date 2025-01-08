from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import types

start_keyboards = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🔎 Wikipedia"), KeyboardButton(text="🌦️ Ob-havo")],
        [KeyboardButton(text="💸 Valyuta"), KeyboardButton(text="🌍 Tarjima")],
        [KeyboardButton(text="🔙 Orqaga")]
    ],
    resize_keyboard=True
)

location_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Lokatsiya jo'natish", request_location=True)]
    ],
    resize_keyboard=True
)


tarjima_kb = types.InlineKeyboardMarkup(inline_keyboard=[
    [types.InlineKeyboardButton("🇺🇿 ▶️ 🇷🇺", callback_data='uz_ru'), types.InlineKeyboardButton("🇷🇺 ▶️ 🇺🇿", callback_data='ru_uz')],
    [types.InlineKeyboardButton("🇺🇸 ▶️ 🇷🇺", callback_data='en_ru'), types.InlineKeyboardButton("🇷🇺 ▶️ 🇺🇸", callback_data='ru_en')],
    [types.InlineKeyboardButton("🇺🇸 ▶️ 🇺🇿", callback_data='en_uz'), types.InlineKeyboardButton("🇺🇿 ▶️ 🇺🇸", callback_data='uz_en')]
])