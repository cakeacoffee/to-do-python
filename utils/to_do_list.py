import json
from utils.item import ListItem
from utils.file_manager import save_to_json_file


class ToDoList:
    name = ""
    items = list()

    def __init__(self, name, items=[]):
        self.name = name
        if items != []:
            self.items = self._convert_item_list(items)
        
        self.save_to_file()

    def add_item_to_list(self, new_items):
        self.items.extend(new_items)
        return self

    def _convert_item_list(self, item_list):
        # Return a list of ListItem
        new_item_list = list()
        for i in item_list:
            new_item_list.append(self._convert_item(i))
        return new_item_list

    def _convert_item(self, item):
        # convert string to list item
        return ListItem(item)
    #! Lernt something
    def to_dict(self):
        return {
            "name": self.name,
            "items": [{"item": item.name, "done": item.done} for item in self.items]
        }

    #! indent?
    def create_json(self):
        return json.dumps(self.to_dict(), indent=4)
    
    def save_to_file(self, file_name: str = "to_do_list.json"):
        save_to_json_file(self.to_dict(), file_name)
