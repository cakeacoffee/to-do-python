import json
from utils.item import ListItem


class ToDoList:
    name = ""
    items = list()

    def __init__(self, name, items=[]):
        self.name = name
        if items != []:
            self.items = self._convert_item_list(items)
        #print(json.loads(self.create_json()))

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

    def create_json(self):
        # return a json as string
        item_str = ""
        for i in self.items:
            item_str += f'{{"item":"{i.name}","done":"{i.done}"}},'
        return f'{{"list": "{self.name}","items":[{item_str}]"}}'
