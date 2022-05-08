"""Prep __main__.py."""
# pylint: disable=invalid-name
from pathlib import Path

import logzero
import typer
from logzero import logger

logzero.loglevel(loglevel())

app = typer.Typer(
    name="{{cookiecutter.pack_name}}",
    add_completion=False,
    help="{{cookiecutter.pack_name help}}",
)


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{app.info.name} v.{__version__} -- ...")
        raise typer.Exit()


@app.command()
def main():
    ...


if __name__ == "__main__":
    app()
