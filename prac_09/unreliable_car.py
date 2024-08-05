"""CP1404 Prac 09 Unreliable Car"""

from car import Car
import random

class UnreliableCar(Car):
    """..."""

    def __init__(self, name, fuel, reliability: float):
        """Initialise a UnreliableCar instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        return f"{super().__str__()}, reliability={self.reliability}"

    def drive(self, distance):
        """Drive like parent Car but calculate fare distance as well."""
        random_number = random.uniform(0, 100)
        if random_number < self.reliability:
            distance_driven = super().drive(distance)
        else:
            distance_driven = 0
        return distance_driven
