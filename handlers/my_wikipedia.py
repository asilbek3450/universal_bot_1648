from aiogram import types
from aiogram.dispatcher import FSMContext
import wikipedia

from states import WikiState


async def wikipediya_f(message: types.Message):
    await message.answer(text="Istalgan so'rov jo'nating: ")
    await WikiState.savol.set()


async def wikipediya_javob(message: types.Message, state: FSMContext):
    savol = message.text
    wikipedia.set_lang('uz')
    try:
        javob = wikipedia.summary(savol)
        await message.answer(f"Siz so'ragan savol: {savol}\n\nJavob:\n{javob}")
    except Exception as xatolik:
        await message.answer(f"XATO CHIQDI: \n{xatolik}")
    await state.finish()


def register_wikipedia_handler(dp):
    dp.register_message_handler(wikipediya_f, text="🔎 Wikipedia")
    dp.register_message_handler(wikipediya_javob, state=WikiState.savol)



