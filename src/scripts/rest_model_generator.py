from pathlib import Path
import json
import re

try:
    with Path.open("../data/nevo_nutrient_data.json") as json_file:
        json_data = json.load(json_file)

        # Extract the keys from the first dictionary in the list
        keys = json_data[0].keys()
        data = ""

        # Create REST API model based on the json file.

        data += "from django.db import models\n\n\n"
        data += "class NutrientData(models.Model):\n"

        # counter = 0

        data += "    nutrient_id = models.IntegerField(primary_key=True)\n"
        for key in keys:
            filter_acids = re.search(r"(F\d*:)", key)
            if not filter_acids:
                data += "    " + key.lower().replace(" ", "_").replace(
                    "_(kj)", ""
                ).replace("_(kcal)", "").replace("_(g)", "").replace(
                    "_(mg)", ""
                ).replace("_(µg)", "").replace(":", "_")
                if key in ["Food group", "Food name", "Quantity"]:
                    data += " = models.CharField(max_length=150)"
                else:
                    data += " = models.DecimalField(max_digits=10, decimal_places=5, default=0,)"
                data += "\n"

        data += "\n    def __str__(self):\n"
        data += "        return self.food_name\n"

        # Writing data to a py file.
        with Path.open("../data/models.py", "w") as file:
            file.write(data)

    print(
        "models.py has been generated, please add the imports or modify other parts if needed."
    )
except FileNotFoundError:
    print("Source file not found.")
