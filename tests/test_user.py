import sys
sys.path.append('../')
import asyncio

from tortoise import run_async
from database.models import UsersModel
from database import initialize


async def get_user():
    users = await UsersModel.all()
    print([region.id for region in users])


async def write_user():
    user = await UsersModel.create(
        id=1,
    )
    print(user)

if __name__ == '__main__':
    run_async(initialize.run_tortoise())
    asyncio.run(write_user())