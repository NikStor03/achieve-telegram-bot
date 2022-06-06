from aiogram import types

from bot.modules.messages.texts import Messages
from bot.modules.states.create_achieve import CreateAchieve
from bot.modules.keyboards.menu_buttons import create_achieve, my_achieves


async def state_monitoring(message: types.Message, state):
    current_state = await state.get_state()
    if message.text in [create_achieve.text, my_achieves.text]:
        text = await Messages.find_text('state-message-error')
        await message.answer(text=text)
        return

    await state.finish()

    if current_state == CreateAchieve.name.state:
        text = await Messages.find_text('create-achieve-day-end')
        await CreateAchieve.end_day.set()
        await message.answer(text=text)
    elif current_state == CreateAchieve.end_day.state:
        text = await Messages.find_text('create-achieve-total-aim')
        await CreateAchieve.total_aim.set()
        await message.answer(text=text)
    elif current_state == CreateAchieve.total_aim.state:
        text = await Messages.find_text('create-achieve-daily-aim')
        await CreateAchieve.daily_aim.set()
        await message.answer(text=text)
    elif current_state == CreateAchieve.daily_aim.state:
        text = await Messages.find_text('create-achieve-short-name')
        await CreateAchieve.short_name.set()
        await message.answer(text=text)
    elif current_state == CreateAchieve.short_name.state:
        text = await Messages.find_text('create-achieve-done')
        await message.answer(text=text)