import sys
sys.path.append('../')
import asyncio

from tortoise import run_async
from database.models import PremiumsPricesModel
from database import initialize


async def get_prices():
    prices = await PremiumsPricesModel.all()
    print([region.price for region in prices])


async def write_prices():
    price = await PremiumsPricesModel.create(
        price=100
    )
    print(price)

if __name__ == '__main__':
    run_async(initialize.run_tortoise())
    asyncio.run(write_prices())