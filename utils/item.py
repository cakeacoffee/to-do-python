from dataclasses import dataclass


@dataclass
class ListItem:
    name: str
    done: bool

    def __init__(self, name: str):
        self.name = name
        self.done = False

    def toggle_done(self):
        self.done = not self.done
