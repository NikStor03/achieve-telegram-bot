import os

from tortoise import run_async

from bot.modules.database.initialize import run_tortoise
from modules.states.create_achieve import CreateAchieve

from core.state_monitoring import state_monitoring
from core.help_message import send_welcome
from core.message_event import message_event

from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware

import logging

from dotenv import load_dotenv
load_dotenv()

logging.basicConfig(
    filename="./logs/logs.log",
    level=logging.INFO,
    format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())

if __name__ == '__main__':
    dp.register_message_handler(
        send_welcome,
        commands=['start', 'help']
    )
    dp.register_message_handler(
        state_monitoring,
        state=CreateAchieve
    )
    dp.register_message_handler(message_event)

    run_async(run_tortoise())
    executor.start_polling(dp, loop=True)
