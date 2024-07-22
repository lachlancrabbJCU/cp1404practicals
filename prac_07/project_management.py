"""
CP1404 Week 07 Practical
Project Management
Start Time: 20.30
End Time:
"""
from project import Project

DEFAULT_FILENAME = "projects.txt"
MENU = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit
"""


def main():
    projects = []
    load_projects(DEFAULT_FILENAME, projects)
    print(projects)
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            pass
        elif choice == "S":
            pass
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            pass
        elif choice == "A":
            add_project(projects)
        elif choice == "U":
            update_project(projects)
        else:
            print("Invalid Choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you for using custom-built project management software.")


def update_project(projects):
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    project_choice = int(input("Project choice: "))
    print(projects[project_choice])
    projects[project_choice].completion_percentage = int(input("New Percentage: "))
    projects[project_choice].priority = int(input("Priority: "))


def display_projects(projects):
    print("Incomplete projects:")
    for project in projects:
        if not project.is_complete():
            print(project)
    print("Complete projects:")
    for project in projects:
        if project.is_complete():
            print(project)


def add_project(projects):
    """Gets new project detail and add it to projects."""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost_estimate: $"))
    completion_percentage = int(input("Percent Complete: "))
    projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))


def load_projects(filename, projects):
    with open(filename, "r") as in_file:
        in_file.readline()  # Consumes first header line
        for line in in_file:
            parts = line.strip().split("\t")
            projects.append(Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4])))
    print(f"Loaded {len(projects)} projects from {filename}")


main()
