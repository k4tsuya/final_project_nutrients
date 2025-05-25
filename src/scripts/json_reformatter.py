"""Script that removes the acids from the json."""

from pathlib import Path
import json
import re

new_list = []

try:
    with open("../data/nevo_nutrient_data.json", "r") as json_file:
        json_data = json.load(json_file)

        for dict in json_data:
            new_dict = {}
            for key, value in dict.items():
                if re.search(r"(F\d*:)", key):
                    pass
                else:
                    new_dict[key] = value
            new_list.append(new_dict)
except FileNotFoundError:
    print("Source file not found.")

try:
    with open("../data/nevo_nutrient_data.json", "w") as json_file:
        json.dump(new_list, json_file, indent=4)
except FileExistsError:
    print("File already exists or file is in use.")
