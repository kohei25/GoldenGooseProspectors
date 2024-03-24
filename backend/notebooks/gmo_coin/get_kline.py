import asyncio
from datetime import datetime, timedelta
from typing import List

import requests
from prisma import Prisma


def get_data(date: datetime, interval: int = 30) -> List:
    date_str = date.strftime("%Y%m%d")
    end_point = "https://api.coin.z.com/public"
    path = f"/v1/klines?symbol=BTC&interval={interval}min&date={date_str}"
    response = requests.get(end_point + path)
    data = response.json()
    return data["data"]


async def add_data(data: List) -> None:
    prisma = Prisma()
    await prisma.connect()
    # async with db.batch_() as batcher:
    for d in data:
        await prisma.btckline.create(
            {
                "openTime": float(d["openTime"]),
                "open": float(d["open"]),
                "high": float(d["high"]),
                "low": float(d["low"]),
                "close": float(d["close"]),
                "volume": float(d["volume"]),
            }
        )
    await prisma.disconnect()


if __name__ == "__main__":
    date = datetime(2021, 4, 17)
    while date < datetime.now():
        date = date + timedelta(days=1)
        data = get_data(date)
        asyncio.run(add_data(data))
