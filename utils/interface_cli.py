"""### CLI Interface
"""

import click
from utils.to_do_list import ToDoList


@click.group()
def cli():
    pass


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
    for i in item:
        print(i)
    items_list = list(item)  # Create list of items with item datatype
    new_list = ToDoList(name, items_list)
    click.echo(f"The new List {new_list.name} was created with the following items:\n")
    for item in new_list.items:
        click.echo(f"{item.name}: done? {item.done}")


# TODO: add functionality
@click.command()
@click.argument("to_do_list")
@click.argument("items", nargs=-1)  # nargs=-1 accepts multiple items as tuple
def add_item(to_do_list, items):
    items_list = list(items)  # tuple to list
    click.echo(f"adding new items {items_list} to list {to_do_list}")


# TODO: add functionality
@click.command
@click.argument("item")
def item_done(item):
    click.echo(f"item {item} a complete")


cli.add_command(create_new_list)
cli.add_command(add_item)
cli.add_command(item_done)
