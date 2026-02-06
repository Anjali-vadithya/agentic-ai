import json
import os


def save_results(data):
    os.makedirs("output", exist_ok=True)

    file_path = "output/results.json"

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    return file_path
