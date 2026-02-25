import json

def load_search_payloads(path: str) -> list[dict]:
    with open(path, "r") as file:
        return json.load(file)