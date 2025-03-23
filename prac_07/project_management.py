"""
CP1404 Practical - 7
Estimated time : 2 hours
Actual time:
Project Management
"""

from prac_07.project import Project
from datetime import datetime

FILENAME = "projects.txt"
MENU = ("- (L)oad projects \n"
        "- (S)ave projects \n"
        "- (D)isplay projects \n"
        "- (F)ilter projects by date) \n"
        "- (A)dd new project\n"
        "- (U)pdate project\n"
        "- (Q)uit")

def main():
    """Program for a project management that track project completion and project details that user wish to complete."""
    projects = load_projects(FILENAME)
    print("Welcome to Pythonic Project Management")
    print(f"Load {len(projects)} projects from {FILENAME}")
    print(MENU)

    choice =input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
           filename = input("Filename: ")
           projects = load_projects(filename)
        elif choice == "S":
            filename = input("Filename: ")
            save_projects(filename, projects)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            date = input("Show projects that start after date (dd/mm/yyyy): ")
            filter_projects_by_date(projects,date)
        elif choice == "A":
            print("Add project")
        elif choice == "U":
            print("Update project")
        else:
            print("Invalid menu choice")
        print(MENU)
        choice = input(">>> ").upper()


def load_projects(filename):
    """Load projects from the txt file and return a list of project objects."""
    projects = []
    with open(filename, "r") as file:
        file.readline() #Skip header line
        for line in file:
            name, start_date, priority, cost_estimate, completion_percentage = line.strip().split('\t')
            projects.append(Project(name,start_date, priority, cost_estimate, completion_percentage))
    return projects

def save_projects(filename, projects):
    """Save the list of projects to the file."""
    with open(filename, "w", newline="") as file:
        file.readline()
        for project in projects:
            file.write(f"{project.name},{project.start_date},{project.priority},{project.cost_estimate},{project.completion_percentage}\n")

def display_projects(projects):
    """Display all projects."""
    incomplete = [project for project in projects if not project.is_complete()]
    complete = [project for project in projects if project.is_complete()]
    print("Incomplete projects: ")
    for project in sorted(incomplete):
        print(f"  {project}")

    print("Complete Projects: ")
    for project in sorted(complete):
        print(f"  {project}")

def filter_projects_by_date(projects,date):
    """Filter and display projects starting after the given date."""
    filter_date = datetime.strptime(date, "%d/%m/%Y").date()
    filtered_projects = [project for project in projects if project.start_date > filter_date]
    print("Filtered projects:")
    for project in sorted(filtered_projects, key=lambda project: project.start_date):
        print(f"  {project}")