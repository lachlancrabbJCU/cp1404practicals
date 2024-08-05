"""CP1404 Prac 09 Taxi Sim."""

from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Simulated taxi service."""
    taxis = [Taxi("Prius", 100), Taxi("Jimbo's Car", 50), SilverServiceTaxi("Fancy Car", 200, 5),
             SilverServiceTaxi("Luxury Car", 200, 10)]

    current_taxi = None
    bill_to_date = 0.0
    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            print("Taxis available:")
            for i, taxi in enumerate(taxis):
                print(f"{i} - {taxi}")
            taxi_choice = get_valid_number("Choose taxi: ")
            if taxi_choice < len(taxis):
                current_taxi = taxi_choice
            else:
                print("Invalid taxi choice")
        elif choice == "D":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                distance = get_valid_number("Drive how far? ")
                taxis[current_taxi].start_fare()
                taxis[current_taxi].drive(distance)
                drive_cost = taxis[current_taxi].get_fare()
                print(f"Your {taxis[current_taxi].name} trip cost you ${drive_cost:.2f}")
                bill_to_date += drive_cost
        else:
            print("Invalid option")
        print(f"Bill to date: ${bill_to_date:.2f}")
        print(MENU)
        choice = input(">>> ").upper()


def get_valid_number(prompt):
    """Get valid integer greater or equal to 0 from user."""
    is_valid_number = False
    while not is_valid_number:
        try:
            number = int(input(prompt))
            if number < 0:
                print("Number must be >= 0")
            else:
                is_valid_number = True
        except ValueError:
            print("Invalid input - please enter a valid number")
    return number  # No risk of being referenced before assignment


if __name__ == '__main__':
    main()
