from aiogram import types

from bot.modules.keyboards.menu_buttons import my_achieves, create_achieve
from bot.modules.messages.texts import Messages
from bot.modules.states.create_achieve import CreateAchieve


async def message_event(message: types.Message):
    if message.text == create_achieve.text:
        await CreateAchieve.name.set()
        text = await Messages.find_text('create-achieve-name')
        await message.answer(text=text)
    elif message.text == my_achieves.text:
        text = await Messages.find_text('achieve-card')
        await message.answer(text=text, parse_mode="HTML")
