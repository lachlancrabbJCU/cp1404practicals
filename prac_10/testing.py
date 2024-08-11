"""
CP1404/CP5632 Practical
Testing demo using assert and doctest
"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    # ((s + " ") * n).strip()  This was my fist thought, also works
    return " ".join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def run_tests():
    """Run the tests on the functions."""
    assert repeat_string("Python", 1) == "Python"
    assert repeat_string("hi", 2) == "hi hi"

    test_car = Car()
    assert test_car._odometer == 0, "Car does not set odometer correctly"
    assert test_car.fuel == 0
    test_car = Car(fuel=10)
    assert test_car.fuel == 10
    test_car.drive(5)
    assert test_car.fuel == 5
    assert test_car._odometer == 5
    test_car.drive(20)  # will only drive 5km
    assert test_car.fuel == 0
    assert test_car._odometer == 10



run_tests()

# (PyCharm may see your >>> doctest comments and run doctests anyway.)
doctest.testmod()


def format_sentence(phrase):
    """
    Function to format a phrase as a sentence starting with a capital and ending with a single full stop.
    >>> format_sentence("hello")
    'Hello.'
    >>> format_sentence("It is an ex parrot.")
    'It is an ex parrot.'
    >>> format_sentence("This is a valid sentence.")
    'This is a valid sentence.'
    """
    parts = phrase.split()
    parts[0] = parts[0].title()
    if parts[-1][-1] != ".":
        parts[-1] = parts[-1] + "."
    return " ".join(parts)



