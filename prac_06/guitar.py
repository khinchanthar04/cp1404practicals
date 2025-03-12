"""
CP1404 Practical - 6
Guitar class
"""

class Guitar:
    def __init__(self, name, year, cost):
        self.name = name
        self.year = year
        self.cost = cost

    def get_age(self):
        return 2022 - self.year  # Change to current year if needed

    def is_vintage(self):
        return self.get_age() >= 50
