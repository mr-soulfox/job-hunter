from prisma import Prisma


class LinksDatabaseVerify:
    @staticmethod
    async def connect(prisma: Prisma, disc: bool = False) -> None:
        if disc:
            await prisma.disconnect()
            return

        await prisma.connect()

    @staticmethod
    async def link_exist(link: str, in_user: bool = False) -> bool:
        database: Prisma = Prisma()
        await LinksDatabaseVerify.connect(database)
        exist: any = None

        if in_user:
            exist = await database.userslisted.find_first(where={
                "url": link
            })

        if not in_user:
            exist = await database.supportedlinks.find_first(where={
                "link": link
            })

        if exist is None:
            await LinksDatabaseVerify.connect(database, True)
            return True

        await LinksDatabaseVerify.connect(database, True)
        return False

    @staticmethod
    async def platform_exist(platform: str) -> bool:
        database: Prisma = Prisma()
        await LinksDatabaseVerify.connect(database)

        exist = await database.supportedlinks.find_unique(where={
            "platform": platform
        })

        if exist is None:
            await LinksDatabaseVerify.connect(database, True)
            return True

        await LinksDatabaseVerify.connect(database, True)
        return False
