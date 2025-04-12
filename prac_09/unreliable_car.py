"""
CP1404 Practical - 9
UnreliableCar class
"""
from random import randint
from prac_09.car import Car

class UnreliableCar(Car):
    """An unreliable version of a car."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar instance."""
        super().__init__(name,fuel)
        self.reliability = reliability

    def drive(self,distance):
        """Drive the car only if it is reliable enough."""
        random_number = randint(1,100)
        if random_number >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven


