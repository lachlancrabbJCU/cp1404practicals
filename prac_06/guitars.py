"""CP1404 Prac 06 guitars.py
Estimate: 1 hour
Actual: 1 hour 15 minutes
"""
from prac_06.guitar import Guitar


def main():
    print("My guitars!")
    guitars = []
    get_guitars(guitars)
    # Test inputs
    # guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    # guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    # guitars.append(Guitar("Fender Stratocaster", 2014, 765.4))

    print_guitars(guitars)


def print_guitars(guitars):
    """Print guitars with proper formating."""
    print("\nThese are my guitars:")
    max_name_width = max(len(guitar.name) for guitar in guitars)
    max_cost_width = max(len(f"{guitar.cost:,.2f}") for guitar in guitars)
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>{max_name_width}} ({guitar.year}), worth ${guitar.cost:{max_cost_width},.2f}"
              f"{vintage_string}")


def get_guitars(guitars):
    """Get guitar information from user until a blank name is entered."""
    is_blank_name = False
    while not is_blank_name:
        name = input("Name: ")
        if name == "":
            is_blank_name = True
        else:
            year = int(input("Year: "))
            cost = float(input("Cost: "))
            print(f"{name} ({year}) : ${cost:,.2f} added.")
            guitars.append(Guitar(name, year, cost))
            print()


main()
