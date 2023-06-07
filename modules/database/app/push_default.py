from prisma import Prisma
from os import path
import json
from modules.database.app.links import Links


async def push_data_default():
    database: Prisma = Prisma()
    await Links.connect(database)

    json_data: dict

    with open(path.join(path.dirname(__file__), "default.json")) as f:
        json_data = json.load(f)
        f.close()

    await database.supportedlinks.create(data={
        'platform': json_data.get("default")["platform"],
        'link': json_data.get("default")["url"]
    })

    await Links.connect(database, True)
