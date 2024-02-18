from rich import print
from datetime import datetime


def date_print(title: str, text: str):
    print(
        f"[bold bright_black]{datetime.now():%Y-%m-%d %H:%M:%S}[/bold bright_black] {title}[white]{str(text)}[/white]"
    )


def debug(text: str):
    date_print(f"[chartreuse3 bold]DEBUG    [/chartreuse3 bold]", f"{str(text)}")


def load(import_: str, message: str):
    date_print(
        f"[yellow bold]MODULE   [/yellow bold]",
        f"[magenta]{import_}[/magenta] {message}",
    )


def online(bot_name: str, message: str):
    date_print(
        f"[green bold]ONLINE   [/green bold]",
        f"[magenta]{bot_name}[/magenta] {message}",
    )
