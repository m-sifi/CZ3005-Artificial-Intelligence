from dataclasses import dataclass
import os
from queue import Queue
import sys
from time import perf_counter
from data import *

# Constexpr function
def MAX_INT():
    return 999999999999
    
@dataclass
class ShortestPath():
    source: str
    destination: str

    total_energy: int
    total_distance: float

    path: list

    # Prints the Shortest Path result in the format that is recommended in the Lab Manual
    def __str__(self):
        path = "->".join([node for node in self.path])
        path_str = f"Shortest path: {self.source}->{path}"
        dist_str = f"Shortest distance: {self.total_distance:.2f}"
        energy_str = f"Total energy cost: {self.total_energy}"

        return f"{path_str}\n{dist_str}\n{energy_str}"

def print_result(results, elapsed, filename):

    if not os.path.exists("out"):
        os.makedirs("out")

    with open(f"out/{filename}.txt", mode="w") as f:
        print(results)
        print(f"\nTime Taken: {elapsed:.3f}s")

        f.write(str(results))
        f.write(f"\n\nTime Taken: {elapsed:.3f}s")

def get_neighbours(v):
    return G[v]

def get_dist(v, w):
    return Dist[f"{v},{w}"]

def get_energy_cost(v, w):
    return Cost[f"{v},{w}"]

def perf_profile(func):
    start = perf_counter()
    result = func()
    end = perf_counter()
    elapsed = end - start

    return (result, elapsed)