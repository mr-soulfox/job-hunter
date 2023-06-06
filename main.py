from typing_extensions import Annotated
import typer
from modules.engine.engine import SearchEngine
from modules.database.app import links
from dotenv import load_dotenv

app = typer.Typer()
load_dotenv()


@app.command()
def main(
        platform: Annotated[str, typer.Option(help="Only linkedin")],
        stack: Annotated[str, typer.Option(help="Stack you wants search")],
        delay: Annotated[int, typer.Option(help="Delay per operation (seconds)")] = 3
):
    search_engine = SearchEngine(
        links.return_link(platform),
        stack,
        delay
    )
    search_engine.search()


if __name__ == "__main__":
    app()
