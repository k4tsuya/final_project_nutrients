from pathlib import Path
import json

with Path.open("../data/nevo_nutrient_data.json") as json_file:
    json_data = json.load(json_file)

    # Extract the keys from the first dictionary in the list
    keys = json_data[0].keys()
    data = ""

    # Create REST API model based on the json file.

    data += "from rest_framework import serializers\n\n"
    data += "class NutrientDataSerializer(serializers.Serializer):\n"

    for key in keys:
        data += "    " + key.lower().replace(" ", "_").replace(
            "_(kj)", ""
        ).replace("_(kcal)", "").replace("_(g)", "").replace(
            "_(mg)", ""
        ).replace("_(µg)", "").replace(":", "_")
        if key in ["Food group", "Food name"]:
            data += " = serializers.CharField(required=True, max_length=50)"
        else:
            data += " = serializers.IntegerField(default=0)"
        data += "\n"

    data += "\nclass NutrientDataSerializer(serializers.ModelSerializer):\n"
    data += "    class Meta:\n"
    data += "        model = Nutrient\n"
    data += '        fields = "__all__"'

    # Writing data to a py file.
    with Path.open("../data/serializers.py", "w") as file:
        file.write(data)

print(
    "serializer.py has been generated, please add the imports or modify other parts if needed."
)
