import sys
from task1 import task_one
from task2.combined_or import distance_or_cost
from task2.combined_and import distance_and_cost
from task2.cost_only import cost_only
from task2.dist_only import distance_only
from task2.naive import naive
from task3.cost_only_manhattan import cost_only_manhattan
from task3.cost_only_euclidian import cost_only_euclidian
from task3.dist_only_manhattan import dist_only_manhattan
from task3.dist_only_euclidian import dist_only_euclidian
from task3.manhattan import manhattan
from task3.euclidian import euclidian

def print_header(label):
    spacing = " " * 4
    label = f"{'=' * 10}{spacing}{label}{spacing}{'=' * 10}"

    print(f"\n{'=' * len(label)}")
    print(label)
    print(f"{'=' * len(label)}\n")

def run_task_one():
    print_header("Task 1: Uniform Cost Search without Energy Constraint")
    task_one()

def run_task_two():
    print_header("Task 2: Uniform Cost Search with Energy Budget (Naive Approach)")
    naive()

    print_header("Task 2: Uniform Cost Search with Energy Budget (Distance Relaxation)")
    distance_only()

    print_header("Task 2: Uniform Cost Search with Energy Budget (Cost Relaxation)")
    cost_only()

    print_header("Task 2: Uniform Cost Search with Energy Budget (Distance AND Cost Relaxation)")
    distance_and_cost()

    print_header("Task 2: Uniform Cost Search with Energy Budget (Distance OR Cost Relaxation)")
    distance_or_cost()

def run_task_three():
    print_header("Task 3: A* Star with Energy Budget (Cost Only + Manhattan Heuristic)")
    cost_only_manhattan()

    print_header("Task 3: A* Star with Energy Budget (Cost Only + Euclidian Heuristic)")
    cost_only_euclidian()

    print_header("Task 3: A* Star with Energy Budget (Distance Only + Euclidian Heuristic)")
    dist_only_euclidian()

    print_header("Task 3: A* Star with Energy Budget (Distance Only + Manhattan Heuristic)")
    dist_only_manhattan()

    print_header("Task 3: A* Star with Energy Budget (Distance OR Cost + Manhattan Heuristic)")
    manhattan()

    print_header("Task 3: A* Star with Energy Budget (Distance OR Cost + Euclidian Heuristic)")
    euclidian()


def main():

    print("\n== CZ3005 Lab Assignment 1 ==\n")
    print("1: Relaxed NYC Problem (No Energy Constraint)")
    print("2: NYC Problem (UCS)")
    print("3: NYC Problem (A* STAR)")
    print("4: Run all")

    option = input("Select an option: ")
    option = option.lower()

    print()

    if option == "1":
        run_task_one()
    elif option == "2":
        run_task_two()
    elif option == "3":
        run_task_three()
    elif option == "4":
        run_task_one()
        run_task_two()
        run_task_three()
    else:
        print("Nothing to do.. exiting")

if __name__ == "__main__":
    main()
