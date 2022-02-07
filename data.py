import json

def load_json(path):
    with open(path) as data:
        return json.load(data)

G = load_json("resources/G.json")
Coord = load_json("resources/Coord.json")
Dist = load_json("resources/Dist.json")
Cost = load_json("resources/Cost.json")

ENERGY_BUDGET = 287932