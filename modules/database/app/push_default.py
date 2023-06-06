from prisma import Prisma
from os import path
import json
from asyncio import run
from modules.database.app.links import Links


def push_data_default():
    database: Prisma = run(Links.connect(Prisma()))
    json_data: dict

    with open(path.join(path.dirname(__file__), "default.json")) as f:
        json_data = json.load(f)
        f.close()

    await database.supportedlinks.create(data={
        'platform': json_data.get("default")["platform"],
        'link': json_data.get("default")["url"]
    })

    await run(Links.connect(database, True))
