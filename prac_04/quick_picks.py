"""Generate quick pick lottery cards"""
import random

MIN_VALUE = 1
MAX_VALUE = 45
NUMBER_RANDOM_NUMBERS = 6


def main():
    number_of_quick_picks = int(input("How many \"quick picks\" do you wish to generate? "))
    for i in range(number_of_quick_picks):
        quick_pick = []
        for j in range(NUMBER_RANDOM_NUMBERS):
            random_int = random.randint(MIN_VALUE, MAX_VALUE)
            while random_int in quick_pick:
                random_int = random.randint(MIN_VALUE, MAX_VALUE)
            quick_pick.append(random_int)
        sorted_quick_pick = sorted(quick_pick)
        for number in sorted_quick_pick:
            print(f"{number:2} ", end="")
        print()




main()
