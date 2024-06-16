"""Generate quick pick lottery cards"""
import random

MIN_VALUE = 1
MAX_VALUE = 45


def main():
    number_of_quick_picks = int(input("How many \"quick picks\" do you wish to generate? "))
    for i in range(number_of_quick_picks):
        for j in range(6):
            print(random.randint(MIN_VALUE, MAX_VALUE), end=" ")
        print()




main()
