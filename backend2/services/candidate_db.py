import json

def load_candidates():
    with open("backend2/data/candidates.json") as f:
        return json.load(f)