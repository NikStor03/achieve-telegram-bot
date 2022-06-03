import sys
sys.path.append('../')
import asyncio

from tortoise import run_async
from database.models import RegionsModel
from database import initialize


async def get_region():
    regions = await RegionsModel.all()
    print([region.name for region in regions])


async def write_region():
    region = await RegionsModel.create(
        name='Asian'
    )
    print(region)

if __name__ == '__main__':
    run_async(initialize.run_tortoise())
    # asyncio.run(get_region())