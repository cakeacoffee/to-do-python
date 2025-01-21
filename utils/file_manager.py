import json


def save_to_json_file(data: dict, file_name: str) -> None:
    with open("data/" + file_name, "w") as outfile:
        json.dump(data, outfile, indent=4)
