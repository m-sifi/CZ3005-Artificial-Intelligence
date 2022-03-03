import json

def load_json(path):
    with open(path) as data:
        return json.load(data)

# Dataset
G = load_json("resources/G.json")
Coord = load_json("resources/Coord.json")
Dist = load_json("resources/Dist.json")
Cost = load_json("resources/Cost.json")

# Constraints 
ENERGY_BUDGET = 287932

# Start and Goal Nodes
START_NODE = "1"
END_NODE = "50"