import asyncio
import datetime
import sys
sys.path.append('../')

from tortoise import run_async
from database.models import AchievesModel
from database import initialize


async def get_achieves():
    regions = await AchievesModel.all()
    print([region.name for region in regions])


async def write_achieves():
    achieve = await AchievesModel.create(
        name='Push Ups',
        descriptions='Achieve push ups',
        end_at=datetime.datetime.now() + datetime.timedelta(days=10)
    )
    print(achieve)

if __name__ == '__main__':
    run_async(initialize.run_tortoise())
    asyncio.run(get_achieves())