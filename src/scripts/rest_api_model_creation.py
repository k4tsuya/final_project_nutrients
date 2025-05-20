from pathlib import Path
import json

with Path.open("../data/nevo_nutrient_data.json") as json_file:
    json_data = json.load(json_file)

    # Extract the keys from the first dictionary in the list
    keys = json_data[0].keys()
    data = ""

    # Create REST API model based on the json file.
    data += "class NutrientData(serializers.Serializer):\n"

    for key in keys:
        data += "    " + key.lower().replace(" ", "_").replace(
            "_(kj)", ""
        ).replace("_(kcal)", "").replace("_(g)", "").replace(
            "_(mg)", ""
        ).replace("_(µg)", "").replace(":", "_")
        if key in ["Food group", "Food name"]:
            data += " = serializers.CharField(required=True, max_length=50)"
        else:
            data += " = serializers.IntegerField(required=True, default=0, blank=False)"
        data += "\n"

    # Writing data to a py file.
    with Path.open("../data/api_model.py", "w") as file:
        file.write(data)
