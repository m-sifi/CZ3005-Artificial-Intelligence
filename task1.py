# Task 1: You will need to solve a relaxed version of the NYC instance where we do not have the energy constraint. 
# You can use any algorithm we discussed in the lectures. 
# Note that this is equivalent to solving the shortest path problem.

from algorithm import dijikstra, Node, ShortestPath

def print_result(shortest_path, filename=None):
    path = "->".join([node for node in shortest_path.path])

    if filename:
        with open(f"out/{filename}.txt", mode="w") as f:
            f.write(f"Shortest path: {shortest_path.source}->{path}\n")
            f.write(f"Shortest distance: {shortest_path.total_distance}\n")
            f.write(f"Total energy cost: {shortest_path.total_energy}\n")
    else:
        print(f"Shortest path: {shortest_path.source}->{path}")
        print(f"Shortest distance: {shortest_path.total_distance}")
        print(f"Total energy cost: {shortest_path.total_energy}")

def task_one():
    result = dijikstra(source="1", destination="50")
    print_result(result, filename="task_1_output")