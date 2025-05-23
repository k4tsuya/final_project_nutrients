"""Script to make the json fixture compatible."""

from pathlib import Path
import json

new_json = []

try:
    with open("../data/nevo_nutrient_data.json", "r") as json_file:
        json_data = json.load(json_file)

        if json_data:
            print("Data loaded.")

        counter = 0
        new_dict = {}

        for item in json_data:
            values = {}
            empty_value = 0
            counter += 1
            new_dict = {
                "model": "nutrient_data.nutrientdata",
                "pk": counter,
                "fields": values,
            }

            for key, value in item.items():
                new_key = ""
                new_key += (
                    key.lower()
                    .replace(" ", "_")
                    .replace("_(kj)", "")
                    .replace("_(kcal)", "")
                    .replace("_(g)", "")
                    .replace("_(mg)", "")
                    .replace("_(µg)", "")
                    .replace(":", "_")
                )

                if value == "":
                    values[new_key] = empty_value
                else:
                    try:
                        values[new_key] = float(value)
                    except ValueError:
                        values[new_key] = value
            new_json.append(new_dict)

except FileNotFoundError:
    print("File not found in specified folder.")

try:
    with open("../data/fixture_data.json", "w") as json_file:
        json.dump(new_json, json_file, indent=4)
        print("Fixture file has been created.")
except:
    print("File couldn't be created.")
