from asyncio import run
from modules.database.app.links import Links
from validators.url import url
import typer
import requests
from modules.engine.scripts.verify_page import verify_if_exist


def verify_errors(platform: str, link: str) -> bool:
    exist = run(Links().platform_exist(platform.lower()))
    link_exist = run(Links().link_exist(link))

    if not exist:
        typer.echo("Platform exist in database")
        return True

    if not link_exist:
        typer.echo("Link exist in database")
        return True

    if not url(link) and not verify_if_exist(requests.get(link)):
        typer.echo("Entrypoint link don't exist or incorrect")
        return True

    return False
