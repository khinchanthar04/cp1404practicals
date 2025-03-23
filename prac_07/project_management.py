"""
CP1404 Practical - 7
Estimated time : 2 hours
Actual time:
Project Management
"""
from prac_07.project import Project

def main():
    projects = load_projects(filename="projects.txt")


def load_projects(filename="projects.txt"):
    """Load projects from the txt file and return a list of project objects."""
    projects = []
    try:
        with open(filename, "r") as file:
            next(file)
            for line in file:
                name, start_date, priority, cost_estimate, completion_percentage = line.strip().split('\t')
                projects.append(Project(name,start_date, priority, cost_estimate, completion_percentage))
        return projects

