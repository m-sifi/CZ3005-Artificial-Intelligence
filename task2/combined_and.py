# # Task 2: You will need to implement an uninformed search algorithm (e.g., the DFS, BFS, UCS) to solve the NYC instance.

from queue import PriorityQueue
from common import *
from data import *

def uniform_cost_search():
    pq      = PriorityQueue()
    min_dist  = { key: float("inf") for key in Coord }
    min_cost  = { key: float("inf") for key in Coord }

    pq.put((0, 0, 0, START_NODE, []))

    while not pq.empty():
        priority, node_dist, node_cost, node, path_to_node = pq.get()

        if node == END_NODE:
            return ShortestPath(total_distance=node_dist, 
                                total_energy=node_cost, 
                                path=path_to_node)

        for neighbour in get_neighbours(node):
            distance = node_dist + get_dist(node, neighbour)
            energy_cost = node_cost + get_energy_cost(node, neighbour)

            if energy_cost > ENERGY_BUDGET:
                continue

            if distance < min_dist[neighbour] and energy_cost < min_cost[neighbour]:
                min_dist[neighbour] = distance
                min_cost[neighbour] = energy_cost

                new_path = path_to_node.copy()
                new_path.append(neighbour)

                new_priority = distance
                pq.put((new_priority, distance, energy_cost, neighbour, new_path))

def distance_and_cost():
    result, elapsed = perf_profile(uniform_cost_search)
    print_result(result, elapsed, "Task2_UCS_Distance_AND_Cost")