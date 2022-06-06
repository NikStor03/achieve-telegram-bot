from aiogram import types

from bot.modules.database.models import UsersModel, PremiumsModel, PremiumsPricesModel
from bot.modules.messages.texts import Messages
from bot.modules.keyboards.menu_buttons import main_menu


async def send_welcome(message: types.Message):
    """
    This command will be called when user sends '/start' or '/help' command
    """
    print('get user')
    user = await UsersModel.get_or_none(user_id=message.from_user.id)

    print(user)
    if user is None:
        price = await PremiumsPricesModel.get_or_none(price=0.0)
        premium = await PremiumsModel.create(
            price=await PremiumsPricesModel.create(price=0.0) if price is None else price
        )
        await UsersModel.create(user_id=message.from_user.id, premium=premium)
    await message.answer(await Messages.find_text('hello'), reply_markup=main_menu)
