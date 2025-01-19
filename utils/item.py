from dataclasses import dataclass


@dataclass
class ListItem:
    name: str
    done: bool

    def __init__(self, name):
        self.name = name
        self.done = False

    def toggle_done(self):
        self.done = not self.done
