# Task 3: You will need to develop an A* search algorithm to solve the NYC instance. The key is to develop a suitable heuristic function for the A* search algorithm in this setting.
from math import dist
from common import *
from queue import PriorityQueue
from data import *

# calculates the heuristic between 2 nodes by computing eucledian distance
def eucledian_distance(start, end):
    start_pos = Coord[start]
    end_pos = Coord[end]

    return dist(start_pos, end_pos)

def a_star():
    pq      = PriorityQueue()
    min_dist  = { key: float("inf") for key in Coord }
    min_cost  = { key: float("inf") for key in Coord }
    min_path = []

    pq.put((0, 0, 0, START_NODE, []))

    while not pq.empty():
        priority, node_dist, node_cost, node, path_to_node = pq.get()

        if node == END_NODE:
            min_path = path_to_node
            break

        for neighbour in get_neighbours(node):
            distance = node_dist + get_dist(node, neighbour)
            energy_cost = node_cost + get_energy_cost(node, neighbour)

            if energy_cost > ENERGY_BUDGET:
                continue

            if distance < min_dist[neighbour] or energy_cost < min_cost[neighbour]:
                min_dist[neighbour] = distance
                min_cost[neighbour] = energy_cost

                new_path = path_to_node.copy()
                new_path.append(neighbour)

                new_priority = distance + eucledian_distance(neighbour, END_NODE)
                pq.put((new_priority, distance, energy_cost, neighbour, new_path))

    return ShortestPath(source=START_NODE, destination=END_NODE, total_distance=min_dist[END_NODE], total_energy=min_cost[END_NODE], path=min_path)

def task_three():
    result, elapsed = perf_profile(a_star)
    print_result(result, elapsed, "3_ASTAR")