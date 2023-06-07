from modules.database.app.exist import LinksDatabaseVerify
from modules.database.user.list.save_list_user import save_list_user
from prisma import Prisma


class DatabaseUserManager(LinksDatabaseVerify):
    @staticmethod
    async def count_users() -> int:
        database: Prisma = Prisma()
        await database.connect()

        quantity: int = await database.userslisted.count()

        await database.disconnect()
        return quantity

    @staticmethod
    async def save_list_user(url: str, connections: int) -> None:
        database: Prisma = Prisma()
        await database.connect()
        await save_list_user(database, url, connections)
