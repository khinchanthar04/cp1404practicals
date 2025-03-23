"""
CP1404 Practical - 7
Estimated time : 2 hours
Actual time:
Project
"""
import datetime

class Project:
    def __init__(self,name,start_date,priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = start_date
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)

