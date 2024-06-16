"""Generate quick pick lottery card with specified number of entries"""
import random

MIN_VALUE = 1
MAX_VALUE = 45
QUICK_PICK_SIZE = 6


def main():
    """Generate and print a quick pick lottery card."""
    number_of_quick_picks = int(input("How many \"quick picks\" do you wish to generate? "))
    for i in range(number_of_quick_picks):
        quick_pick = generate_quick_pick()
        print_quick_pick(quick_pick)
        print()


def print_quick_pick(quick_pick):
    """Print formatted quick pick with correct spacing."""
    for number in quick_pick:
        print(f"{number:2} ", end="")


def generate_quick_pick():
    """Generate sorted list of QUICK_PICK_SIZE unique random numbers between MIN_VALUE and MAX_VALUE."""
    unsorted_quick_pick = []
    for j in range(QUICK_PICK_SIZE):
        random_number = random.randint(MIN_VALUE, MAX_VALUE)
        while random_number in unsorted_quick_pick:
            random_number = random.randint(MIN_VALUE, MAX_VALUE)
        unsorted_quick_pick.append(random_number)
    quick_pick = sorted(unsorted_quick_pick)
    return quick_pick


main()
