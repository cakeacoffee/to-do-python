from dataclasses import dataclass


@dataclass
class ListItem:
    """### ListItem Data Object"""

    name: str
    done: bool

    def __init__(self, name: str):
        """
        Args:
            name (str): the name of the item
        """
        self.name = name
        self.done = False

    def toggle_done(self) -> None:
        """toggle done between true and false (done and not done)"""
        self.done = not self.done
