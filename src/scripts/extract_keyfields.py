from pathlib import Path
import json
import re

with Path.open("../data/nevo_nutrient_data.json") as json_file:
    json_data = json.load(json_file)

    # Extract the keys from the first dictionary in the list
    keys = json_data[0].keys()
    data = ""

    # Print and add the keys to data variable.
    print("Keys in the JSON data:")
    for key in keys:
        exclude_acids = re.match(r"(F\d*:)", key)
        if not exclude_acids:
            data += key + "\n"
            print(key)

    # Writing data to a text file.
    with Path.open("../data/keyfields.txt", "w") as file:
        file.write(data)
