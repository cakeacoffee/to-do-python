"""### File Manager
    Includes functions:
        *  save_to_json_file(data: dict, file_name: str) -> None:
"""

import json


def save_to_json_file(data: dict, file_name: str) -> None:
    """### Save dictionary to json file

    #### Args:
        `data (dict): the dictionary`
        `file_name (str): the file name`
    """
    with open("data/" + file_name, "w") as outfile:
        json.dump(data, outfile, indent=4)
