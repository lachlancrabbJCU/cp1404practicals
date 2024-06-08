"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
    ValueError will occur something that can not me turned into
    an int is input to numerator or denominator e.g. "seven" or "7.0"

2. When will a ZeroDivisionError occur?
    ZeroDivisionError will occur on the "fraction = numerator / denominator"
    line if denominator == 0

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    A check would be added to get non-zero int, with a while loop
    e.g. while denominator == 0:
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Denominator must not be zero")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
