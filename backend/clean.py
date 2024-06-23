import json
import re

# Load the JSON file
with open('data/hashtags.json') as file:
    data = json.load(file)

# Remove non-alphanumeric keys
cleaned_data = {key: value for key, value in data.items() if re.match(r'^[a-zA-Z0-9]+$', key)}

# Save the modified JSON back to a file
with open('data/hashtags.json', 'w') as file:
    json.dump(cleaned_data, file, indent=4)

print("\u0440\u0435\u043a".isalnum())