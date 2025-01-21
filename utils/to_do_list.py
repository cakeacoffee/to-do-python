import json
from utils.item import ListItem
from utils.file_manager import save_to_json_file


class ToDoList:
    name = ""
    items = list()

    def __init__(self, name: str, items: list[str] = None):
        self.name = name
        self.items = self._convert_item_list(items) if items else []

        self.save_to_file()

    # TODO: new_items is a list of strings, convert with _convert_item_list
    def add_item_to_list(self, new_items: list[str]):
        self.items.extend(new_items)
        return self

    def _convert_item_list(self, item_list: list[str]) -> list[ListItem]:
        new_item_list = list()
        for i in item_list:
            new_item_list.append(self._convert_item(i))
        return new_item_list

    def _convert_item(self, item: str) -> ListItem:
        return ListItem(item)

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "items": [{"item": item.name, "done": item.done} for item in self.items],
        }

    def create_json(self) -> str:
        return json.dumps(self.to_dict(), indent=4)

    def save_to_file(self, file_name: str = "to_do_list.json") -> None:
        save_to_json_file(self.to_dict(), file_name)
