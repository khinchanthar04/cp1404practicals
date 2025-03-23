"""
CP1404 Practical - 7
Estimated time : 2 hours
Actual time:
Project
"""
import datetime

class Project:
    """
    A class to represent a project.
    """
    def __init__(self,name,start_date,priority, cost_estimate, completion_percentage):
        """Initialize a project object with given attributes."""
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)

    def __str__(self):
        """Return a string representation of the project."""
        return (f"{self.name}, start: {self.start_date.strftime("%d/%m/%Y")}, priority:{self.priority}, "
                f"cost: {self.cost_estimate:.2f}. completion: {self.completion_percentage}%")

    def __lt__(self, other):
        """Define less than operator for sorting by priority."""
        return self.priority < other.priority

    def is_completed (self):
        """Check if the project is completed."""
        return self.completion_percentage == 100

    def update(self, new_completion_percentage = None, new_priority = None):
        if new_completion_percentage is not None:
            self.completion_percentage = int(new_completion_percentage)
        if new_priority is not None:
            self.priority = int(new_priority)