from asyncio import run

import typer
from dotenv import load_dotenv
from typing_extensions import Annotated
from validators.url import url

from modules.Errors.add_command import verify_errors
from modules.database.app.links import Links
from modules.database.app.push_default import push_data_default
from modules.engine.engine import SearchEngine

app = typer.Typer()
load_dotenv()

default_is_loaded = run(Links().return_link(platform="linkedin"))
if not default_is_loaded:
    run(push_data_default())


@app.command()
def main(
        platform: Annotated[str, typer.Option(help="Only linkedin")],
        stack: Annotated[str, typer.Option(help="Stack you wants search")],
        delay: Annotated[int, typer.Option(help="Delay per operation (seconds)")] = 3
) -> None:
    link = run(Links().return_link(platform))

    if url(link):
        search_engine = SearchEngine(link, stack, delay)
        search_engine.search()
        return

    typer.echo("URL In database invalid")


@app.command("add")
def add(
    platform: Annotated[str, typer.Option(help="Platform name")],
    link: Annotated[str, typer.Option(help="Entrypoint to start operation")]
) -> None:
    exist_errors = verify_errors(platform=platform, link=link)
    if not exist_errors:
        print("success")

    return


if __name__ == "__main__":
    app()
