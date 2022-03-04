# Task 1: You will need to solve a relaxed version of the NYC instance where we do not have the energy constraint. 
# You can use any algorithm we discussed in the lectures. 
# Note that this is equivalent to solving the shortest path problem.

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

            if distance < min_dist[neighbour] or energy_cost < min_cost[neighbour]:
                min_dist[neighbour] = distance
                min_cost[neighbour] = energy_cost

                new_path = path_to_node.copy()
                new_path.append(neighbour)

                new_priority = distance
                pq.put((new_priority, distance, energy_cost, neighbour, new_path))

def task_one():
    result, elapsed = perf_profile(uniform_cost_search)
    print_result(result, elapsed, "1")