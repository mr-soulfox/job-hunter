from asyncio import run
from prisma import Prisma
from validators import url


class Links:
    @staticmethod
    async def connect(prisma: Prisma, disc: bool = False) -> None:
        if disc:
            await prisma.disconnect()
            return

        await prisma.connect()

    @staticmethod
    async def return_link(platform: str) -> bool or str:
        database: Prisma = Prisma()
        await Links.connect(database)

        supported = await database.supportedlinks.find_unique(where={'platform': platform})
        if supported is None:
            return True

        if url(supported.link):
            await Links.connect(database, True)
            return supported.link

        await Links.connect(database, True)
        return False

    @staticmethod
    async def link_exist(link: str) -> bool:
        database: Prisma = Prisma()
        await Links.connect(database)

        exist = await database.supportedlinks.find_first(where={
            "link": link
        })

        if exist is None:
            await Links.connect(database, True)
            return True

        await Links.connect(database, True)
        return False

    @staticmethod
    async def platform_exist(platform: str) -> bool:
        database: Prisma = Prisma()
        await Links.connect(database)

        exist = await database.supportedlinks.find_unique(where={
            "platform": platform
        })

        if exist is None:
            await Links.connect(database, True)
            return True

        await Links.connect(database, True)
        return False

    @staticmethod
    async def save_link(platform: str = "", link: str = "") -> bool:
        database: Prisma = Prisma()
        await Links.connect(database)

        if bool(url(link)):
            await database.supportedlinks.create(data={
                'platform': platform.lower(),
                'link': link
            })

            await Links.connect(database, True)
            return True

        await Links.connect(database, True)
        return False
