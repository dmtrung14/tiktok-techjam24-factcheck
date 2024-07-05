from backend.config import Config
from transformers import pipeline
import json
import re

# Load the JSON file
def clean_hashtags():
    with open('data/hashtags.json') as file:
        data = json.load(file)

    # Remove non-alphanumeric keys
    cleaned_data = {key: value for key, value in data.items() if re.match(r'^[a-zA-Z0-9]+$', key) and len(key) > 1 and not any(f in key for f in Config.Explorer.filter)}

    # Save the modified JSON back to a file
    with open('data/hashtags.json', 'w') as file:
        json.dump(cleaned_data, file, indent=4)

def reduce_hashtags():
    with open('data/hashtags.json') as file:
        data = json.load(file)
    threshold = 0.75
    filter = Config.Explorer.filter

    new_hash_tags = {
        
    }
    for key in data:
        if data[key] < threshold or any(f in key for f in filter) or len(key) == 1:
            continue
        new_hash_tags[key] = 1
        
    with open('data/reduced_hashtags.json', 'w') as file:
        json.dump(new_hash_tags, file, indent=4)


if __name__ == "__main__":
    clean_hashtags()
    reduce_hashtags()