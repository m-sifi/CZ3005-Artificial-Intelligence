# Task 3: You will need to develop an A* search algorithm to solve the NYC instance. The key is to develop a suitable heuristic function for the A* search algorithm in this setting.
from common import *
from queue import PriorityQueue
from data import *

def manhattan_distance(start, end):
    start_pos = Coord[start]
    end_pos = Coord[end]

    return abs(start_pos[0] - end_pos[0]) + abs(start_pos[1] - end_pos[1])

def a_star():
    pq      = PriorityQueue()
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

            if energy_cost < min_cost[neighbour]:
                min_cost[neighbour] = energy_cost

                new_path = path_to_node.copy()
                new_path.append(neighbour)

                new_priority = distance + manhattan_distance(neighbour, END_NODE)
                pq.put((new_priority, distance, energy_cost, neighbour, new_path))

def cost_only_manhattan():
    result, elapsed = perf_profile(a_star)
    print_result(result, elapsed, "Task3_Cost_Manhattan")