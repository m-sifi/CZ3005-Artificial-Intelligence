from dataclasses import dataclass, field
from queue import PriorityQueue
from data import G, Dist, Coord, Cost

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

def dijikstra(source, destination, weight_dict=Dist):
    pq = PriorityQueue()
    dist = {key: MAX_INT() for key in Coord }
    cost = {key: MAX_INT() for key in Coord }
    parent = { key: "-1" for key in Coord }

    source_idx = source
    destination_idx = destination

    node = Node(0, source_idx)
    dist[source_idx] = 0
    cost[source_idx] = 0
    parent[source_idx] = "-1"

    pq.put(node)

    while pq.empty() is False:
        node = pq.get()
        neighbours = G[node.item]

        for v in neighbours:
            weight = Dist[f"{node.item},{v}"]

            if(dist[v] > dist[node.item] + weight):
                dist[v] = dist[node.item] + weight
                cost[v] = cost[node.item] + Cost[f"{node.item},{v}"]
                parent[v] = node.item

                pq.put(Node(priority=dist[v], item=v))

    path = get_path(parent=parent, dest=destination_idx, path=[])

    return ShortestPath(
        source=source_idx, 
        destination=destination_idx, 
        total_distance=dist[destination_idx],
        total_energy=cost[destination_idx],
        path=path)