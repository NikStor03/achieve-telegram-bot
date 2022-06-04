from tortoise import Tortoise
from database import models
import os
from dotenv import load_dotenv
load_dotenv()


async def run_tortoise():
    uri = os.getenv("DATABASE_URI")

    await Tortoise.init(db_url=uri, modules={'models': [models]})
    await Tortoise.generate_schemas()
