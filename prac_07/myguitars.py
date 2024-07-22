"""
CP1404 Week 07 Practical
My Guitars
Start Time: 19:40
End Time: 20:
"""
from guitar import Guitar
import csv

FILENAME = "guitars.csv"


def main():
    print("My guitars!")
    guitars = []
    load_guitars(guitars)
    display_guitars(guitars.sort())


def load_guitars(guitars):
    """Guitar file reader version using the csv module."""
    in_file = open(FILENAME, 'r', newline='')
    reader = csv.reader(in_file)  # use default dialect, Excel
    for row in reader:
        guitars.append(Guitar(row[0], int(row[1]), float(row[2])))
    in_file.close()


def display_guitars(guitars):
    """Print list of guitars with proper formatting."""
    print("\nThese are my guitars:")
    max_name_width = max(len(guitar.name) for guitar in guitars)
    max_cost_width = max(len(f"{guitar.cost:,.2f}") for guitar in guitars)
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>{max_name_width}} ({guitar.year}), worth ${guitar.cost:{max_cost_width},.2f}"
              f"{vintage_string}")


main()
