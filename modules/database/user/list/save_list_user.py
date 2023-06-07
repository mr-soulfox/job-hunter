from modules.database.user.database_manager import DatabaseUserManager
from prisma import Prisma

user_list_params = {
    "url": str,
    "connections": int
}


def save_list_user(database: Prisma, url: str, connections: int):
    exist: bool = await DatabaseUserManager.link_exist(url, True)

    if exist:
        await database.userslisted.create(data={
            "url": url,
            "connections": connections
        })
