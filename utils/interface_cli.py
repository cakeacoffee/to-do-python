"""### CLI Interface
"""

import click
from utils.to_do_list import ToDoList
from utils.db_setup import *


@click.group()
def cli():
    pass


@click.command()
def show_all() -> None:
    print(show_db())
    click.echo(show_db())


@click.command()
@click.argument("name")
@click.option("--item", multiple=True, help="items in list")
def create_new_list(name: str, item: str) -> None:
    """### Create a new to do list
        cli interface for creating a new to-do-list

    Args:
        `name (str): to do list name`
        `item (str): item name`
    """
    message = initialize_database()
    message += add_list(name)
    for i in item:
        message += add_item(i,name)
    click.echo(message)



@click.command()
@click.argument("to_do_list")
@click.argument("items", nargs=-1)  # nargs=-1 accepts multiple items as tuple
def add_item_to_list(to_do_list, items):
    message = ""
    for i in items:
        message += add_item(i, to_do_list)
    click.echo(message)


# TODO: add functionality
@click.command
@click.argument("item")
def item_done(item):
    click.echo(f"item {item} a complete")


cli.add_command(create_new_list)
cli.add_command(add_item_to_list)
cli.add_command(item_done)
cli.add_command(show_all)
