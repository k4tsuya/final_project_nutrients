import csv
import json
from pathlib import Path

try:
    with Path.open("../data/nevo_nutrient_data.csv", "r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data = []
        for row in csv_reader:
            # Convert the row to a dictionary and append it to the list
            data.append(row)
        # Convert the list of dictionaries to a JSON string
        json_data = json.dumps(data, indent=4)
        # Write the JSON string to a file
        with Path.open("../data/nevo_nutrient_data.json", "w") as json_file:
            json_file.write(json_data)
        print("CSV data has been converted to JSON as nevo_nutrient_data.json")
except FileNotFoundError:
    print("The specified CSV file was not found.")
