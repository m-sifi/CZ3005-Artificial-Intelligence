# Task 2: You will need to implement an uninformed search algorithm (e.g., the DFS, BFS, UCS) to solve the NYC instance.

from cmath import cos
from algorithm import *
from common import print_result
from queue import PriorityQueue
from data import ENERGY_BUDGET, G, Dist, Coord, Cost

from task1 import dijikstra

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
            new_cost = cost[node.item] + weight

            if new_cost > ENERGY_BUDGET:
                continue

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

# modified dijikstra with constraint satisfaction
def dijikstra_energy(source, destination):
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
            weight = Cost[f"{node.item},{v}"]
            new_cost = cost[node.item] + weight

            # forward checking
            if(new_cost <= ENERGY_BUDGET and cost[v] > new_cost):
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

def task_two():
    shortest_distance = dijikstra(source="1", destination="50")
    smallest_cost = dijikstra_energy(source="1", destination="50")

    if(shortest_distance.total_energy < smallest_cost.total_energy):
        print_result(shortest_distance, filename="task_2_nyc_solution")
    else:
        print_result(smallest_cost, filename="task_2_nyc_solution")

    print_result(shortest_distance, filename="task_2_dist")
    print_result(smallest_cost, filename="task_2_cost")