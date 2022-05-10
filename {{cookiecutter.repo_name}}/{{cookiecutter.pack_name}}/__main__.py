"""Prep __main__.py."""
# pylint: disable=invalid-name
from pathlib import Path
from typing import Optional

import logzero
import typer
from logzero import logger
from set_loglevel import set_loglevel

from {{cookiecutter.pack_name}} import __version__, {{cookiecutter.pack_name}}

logzero.loglevel(set_loglevel())

app = typer.Typer(
    name="{{cookiecutter.pack_name}}",
    add_completion=False,
    help="{{cookiecutter.pack_name}} help",
)


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{app.info.name} v.{__version__} -- ...")
        raise typer.Exit()


@app.command()
def main(
    version: Optional[bool] = typer.Option(  # pylint: disable=(unused-argument
        None,
        "--version",
        "-v",
        "-V",
        help="Show version info and exit.",
        callback=_version_callback,
        is_eager=True,
    ),
):
    """Define."""
    ...


if __name__ == "__main__":
    app()
