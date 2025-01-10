from aiogram import types
from aiogram import Dispatcher
from config import OBHAVO_KEY
from keyboards import location_keyboard, start_keyboards
import requests


async def ob_havo_handler(message: types.Message):
    await message.answer(text="Siz ob-havo bo'limiga kirdingiz, obhavoni bilish uchun lokatsiya jo'nating", reply_markup=location_keyboard)

async def lokatsiya_handler(message: types.Message):
    latitude = message.location.latitude
    longitude = message.location.longitude
    url = "https://weatherapi-com.p.rapidapi.com/current.json"
    querystring = {"q":f"{latitude},{longitude}"}
    headers = {
        "x-rapidapi-key": "0e1e80d5bfmsh213ed89c8e67ef5p10d6b3jsn0c4cbb51f1b1",
        "x-rapidapi-host": "weatherapi-com.p.rapidapi.com"
    }
    data = requests.get(url, headers=headers, params=querystring).json()

    location = data['location']
    current = data['current']
    
    # Kerakli ma'lumotlar
    name = location.get('name', 'Noma’lum')  # Joy nomi
    temp_c = current.get('temp_c', 'Noma’lum')  # Havo harorati
    condition = current.get('condition', {}).get('text', 'Noma’lum')  # Ob-havo holati
    wind_kph = current.get('wind_kph', 'Noma’lum')  # Shamol tezligi
    humidity = current.get('humidity', 'Noma’lum')  # Namlik darajasi
    
    # Javobni botga yuborish
    await message.answer(
        f"🌍 Joy: {name}\n"
        f"🌡️ Harorat: {temp_c}°C\n"
        f"☀️ Ob-havo: {condition}\n"
        f"💨 Shamol tezligi: {wind_kph} km/soat\n"
        f"💧 Namlik: {humidity}%",
        reply_markup=start_keyboards
    )


def register_obhavo_handler(dp: Dispatcher):
    dp.register_message_handler(ob_havo_handler, text="🌦️ Ob-havo")
    dp.register_message_handler(lokatsiya_handler, content_types=types.ContentType.LOCATION)

