from algorithm import ShortestPath

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