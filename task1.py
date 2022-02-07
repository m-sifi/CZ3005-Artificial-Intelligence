# Task 1: You will need to solve a relaxed version of the NYC instance where we do not have the energy constraint. 
# You can use any algorithm we discussed in the lectures. 
# Note that this is equivalent to solving the shortest path problem.

from algorithm import *
from common import print_result
from queue import PriorityQueue
from data import G, Dist, Coord, Cost

def dijikstra(source, destination):
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

def task_one():
    result = dijikstra(source="1", destination="50")
    print_result(result, filename="task_1_output")