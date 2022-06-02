import os
from tortoise import Tortoise
import models


async def run_tortoise():
    uri = os.getenv("DATABASE_URI", default=None)

    await Tortoise.init(db_url=uri, modules={'models': [models]})
    await Tortoise.generate_schemas()