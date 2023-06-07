from asyncio import run

import typer
from dotenv import load_dotenv
from typing_extensions import Annotated

from modules.Errors.add_command import verify_errors
from modules.database.app.links import Links
from modules.database.app.push_default import push_data_default
from modules.engine.engine import SearchEngine

app = typer.Typer()
load_dotenv()


@app.command("run")
def main(
        platform: Annotated[str, typer.Option(help="Only linkedin")],
        stack: Annotated[str, typer.Option(help="Stack you wants search")],
        delay: Annotated[int, typer.Option(help="Delay per operation (seconds)")] = 3,
        scroll: Annotated[int, typer.Option(help="Quantity of scroll down repeats")] = 5
) -> None:
    if run(Links().platform_exist(platform)):
        link: str = run(Links().return_link(platform=platform.lower()))

        search_engine = SearchEngine(link, platform, stack, scroll, delay)
        search_engine.search()
        return

    typer.echo("Platform don't exist")


@app.command("add")
def add(
    platform: Annotated[str, typer.Option(help="Platform name")],
    link: Annotated[str, typer.Option(help="Entrypoint to start operation")]
) -> None:
    exist_errors = verify_errors(platform=platform, link=link)

    if not exist_errors:
        run(Links().save_link(platform=platform, link=link))

    return


@app.command("load-default")
def load_default() -> None:
    default_is_loaded: bool or str = run(Links().return_link(platform="linkedin"))

    if default_is_loaded:
        run(push_data_default())


if __name__ == "__main__":
    app()
