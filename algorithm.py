from dataclasses import dataclass, field

# constexpr
def MAX_INT():
    return 999999999999

@dataclass(order=True)
class Node:
    priority: int
    item: str = field(compare=False)

@dataclass
class ShortestPath():
    source: str
    destination: str

    total_energy: int
    total_distance: float

    path: list

def get_path(parent, dest, path):

    if(parent[dest] == "-1"):
        return path

    path = get_path(parent, parent[dest], path)
    path.append(dest)

    return path