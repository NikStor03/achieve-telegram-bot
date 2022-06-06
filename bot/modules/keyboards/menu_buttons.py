from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(resize_keyboard=False)
create_achieve = KeyboardButton('Create achieve')
my_achieves = KeyboardButton('My achieves')
main_menu.add(create_achieve, my_achieves)

