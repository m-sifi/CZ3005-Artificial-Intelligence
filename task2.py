# Task 2: You will need to implement an uninformed search algorithm (e.g., the DFS, BFS, UCS) to solve the NYC instance.

from cmath import cos
from algorithm import *
from common import print_result
from queue import PriorityQueue
from data import ENERGY_BUDGET, G, Dist, Coord, Cost

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
            new_dist = dist[node.item] + Dist[f"{node.item},{v}"]
            new_cost = cost[node.item] + Cost[f"{node.item},{v}"]

            if new_cost > ENERGY_BUDGET:
                continue

            if(dist[v] > new_dist and cost[v] > new_cost):
                dist[v] = new_dist
                cost[v] = new_cost
                parent[v] = node.item

                pq.put(Node(priority=dist[v], item=v))

    path = get_path(parent=parent, dest=destination_idx, path=[])

    return ShortestPath(
        source=source_idx, 
        destination=destination_idx, 
        total_distance=dist[destination_idx],
        total_energy=cost[destination_idx],
        path=path)

def task_two():
    solution = dijikstra(source="1", destination="50")
    print_result(solution, filename="task_2_nyc_solution_final")