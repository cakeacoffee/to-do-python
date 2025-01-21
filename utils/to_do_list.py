import json
from utils.item import ListItem
from utils.file_manager import save_to_json_file


class ToDoList:
    """ToDoList class
    """
    name = ""
    items = list()

    def __init__(self, name: str, items: list[str] = None):
        """
        Initialize a ToDoList with a name and optional list of items

        Args:
            name (str): name of the to-do list.
            items (list[str], optional): a list of item names. defaults to None.
        """
        self.name = name
        self.items = self._convert_item_list(items) if items else []

        self.save_to_file()

    # TODO: new_items is a list of strings, convert with _convert_item_list
    def add_item_to_list(self, new_items: list[str]):
        self.items.extend(new_items)
        return self

    def _convert_item_list(self, item_list: list[str]) -> list[ListItem]:
        """### Convert item to list
        convert a list of strings into ListItem objects

        Args:
            `item_list (list[str]): list of item names`

        Returns:
            `list[ListItem]: a list of ListItem objects`
        """
        new_item_list = list()
        for i in item_list:
            new_item_list.append(self._convert_item(i))
        return new_item_list

    def _convert_item(self, item: str) -> ListItem:
        """### Convert item
        convert a string into a ListItem object

        Args:
            `item (str): the name of the item`

        Returns:
            `ListItem: the corresponding ListItem object`
        """
        return ListItem(item)

    def to_dict(self) -> dict:
        """### To Dictionary
        convert the ToDoList instance into a dictionary

        Returns:
            `dict: Dictionary representation of the to-do list`
        """
        return {
            "name": self.name,
            "items": [{"item": item.name, "done": item.done} for item in self.items],
        }

    def create_json(self) -> str:
        """### Create JSON
        convert the ToDoList instance into a JSON string

        Returns:
            `str: JSON string representation of the to-do list`
        """
        return json.dumps(self.to_dict(), indent=4)

    def save_to_file(self, file_name: str = "to_do_list.json") -> None:
        """### Save to File
        save the ToDoList instance to a JSON file

        Args:
            `file_name (str, optional): name of the file. Defaults to "to_do_list.json"`
        """
        save_to_json_file(self.to_dict(), file_name)
