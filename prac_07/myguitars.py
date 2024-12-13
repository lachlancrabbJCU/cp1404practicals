"""
CP1404 Week 07 Practical
My Guitars
Start Time: 19:40
End Time: 20:20
"""
from guitar import Guitar
import csv

FILENAME = "guitars.csv"


def main():
    print("My guitars!")
    guitars = []
    load_guitars(guitars)
    get_guitars(guitars)
    guitars.sort()
    print_guitars(guitars)
    save_guitars(guitars)


def load_guitars(guitars):
    """Guitar file reader using the csv module."""
    in_file = open(FILENAME, 'r', newline='')
    reader = csv.reader(in_file)  # use default dialect, Excel
    for row in reader:
        guitars.append(Guitar(row[0], int(row[1]), float(row[2])))
    in_file.close()


def get_guitars(guitars):
    """Get guitar information from user until a blank name is entered."""
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        print(f"{name} ({year}) : ${cost:,.2f} added.")
        guitars.append(Guitar(name, year, cost))
        print()
        name = input("Name: ")


def print_guitars(guitars):
    """Print list of guitars with proper formatting."""
    print("\nThese are my guitars:")
    max_name_width = max(len(guitar.name) for guitar in guitars)
    max_cost_width = max(len(f"{guitar.cost:,.2f}") for guitar in guitars)
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>{max_name_width}} ({guitar.year}), worth ${guitar.cost:{max_cost_width},.2f}"
              f"{vintage_string}")


def save_guitars(guitars):
    """Guitar file writer using the csv module."""
    out_file = open(FILENAME, 'w', newline="")
    writer = csv.writer(out_file)
    for guitar in guitars:
        writer.writerow([guitar.name, guitar.year, guitar.cost])
    out_file.close()


main()
