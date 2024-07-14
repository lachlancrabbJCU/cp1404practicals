"""CP1404 Prac 06 guitar_test.py"""
from prac_06.guitar import Guitar


def main():
    """Test Guitar class."""
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    other_guitar = Guitar("Another Guitar", 2000, 68419.11)
    vintage_guitar = Guitar("50-Year old guitar", 1974, 5050.50)

    print_age_test(gibson, 102)
    print_age_test(other_guitar, 24)
    print_age_test(vintage_guitar, 50)
    print_vintage_test(gibson, True)
    print_vintage_test(other_guitar, False)
    print_vintage_test(vintage_guitar, True)


def print_age_test(guitar, expected_age):
    """Test get_age function for the Guitar class."""
    print(f"{guitar.name} get_age() - Expected {expected_age}. Got {guitar.get_age()}")


def print_vintage_test(guitar, is_vintage_expected):
    """Test is_vintage function for the Guitar class."""
    print(f"{guitar.name} is_vintage() - Expected {is_vintage_expected}. Got {guitar.is_vintage()}")


main()
