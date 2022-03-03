import sys
from task1 import task_one
from task2 import task_two
from task3 import task_three

def print_header(label):
    spacing = " " * 4
    label = f"{'=' * 10}{spacing}{label}{spacing}{'=' * 10}"

    print(f"\n{'=' * len(label)}")
    print(label)
    print(f"{'=' * len(label)}\n")

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
        print_header("Task 1: Uniform Cost Search without Energy Constraint")
        task_one()
    elif option == "2":
        print_header("Task 2: Uniform Cost Search with Energy Budget")
        task_two()
    elif option == "3":
        print_header("Task 3: A* Star with Energy Budget")
        task_three()
    elif option == "4":
        print_header("Task 1: Uniform Cost Search without Energy Constraint")
        task_one()
        print_header("Task 2: Uniform Cost Search with Energy Budget")
        task_two()
        print_header("Task 3: A* Star with Energy Budget")
        task_three()
    else:
        print("Nothing to do.. exiting")

if __name__ == "__main__":
    main()
