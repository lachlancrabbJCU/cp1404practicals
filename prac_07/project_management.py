"""
CP1404 Week 07 Practical
Project Management
Start Time: 20.30
End Time:
"""
from project import Project
import datetime

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
            filename = input("Filename: ")
            load_projects(filename, projects)
        elif choice == "S":
            filename = input("Filename: ")
            save_projects(filename, projects)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_projects(projects)
        elif choice == "A":
            add_project(projects)
        elif choice == "U":
            update_project(projects)
        else:
            print("Invalid Choice")
        print(MENU)
        choice = input(">>> ").upper()
    save_query = input(f"Would you like to save to {DEFAULT_FILENAME}?").upper()
    if save_query == "" or save_query == "Y" or save_query == "YES":
        save_projects(DEFAULT_FILENAME, projects)
    print("Thank you for using custom-built project management software.")


def filter_projects(projects):
    """Get date, display only the projects with start dates after that date."""
    filter_date_string = input("Show projects that start after date (dd/mm/yy):")
    filter_date = datetime.datetime.strptime(filter_date_string, "%d/%m/%y").date()
    filtered_projects = [project for project in projects if project.start_date > filter_date]
    filtered_projects.sort()
    for project in filtered_projects:
        print(project)


def update_project(projects):
    """Choose a project then update the completion percent and priority."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    project_choice = get_valid_number("Project choice: ")
    while project_choice > len(projects):
        print("Invalid project number")
        project_choice = get_valid_number("Project choice: ")
    print(projects[project_choice])
    new_completion_percentage = get_valid_number("New Percentage: ")
    while new_completion_percentage < 100:
        print("Invalid percentage")
        new_completion_percentage = get_valid_number("New Percentage: ")
    projects[project_choice].completion_percentage = new_completion_percentage
    projects[project_choice].priority = get_valid_number("Priority: ")


def display_projects(projects):
    """Display Project info."""
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
    name = get_valid_string("Name: ")
    start_date = datetime.datetime.strptime(input("Start date (dd/mm/yy): "), "%d/%m/%y").date()
    priority = get_valid_number("Priority: ")
    cost_estimate = float(input("Cost_estimate: $"))
    completion_percentage = int(input("Percent Complete: "))
    projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))


def load_projects(filename, projects):
    """Load project from filename."""
    with open(filename, "r") as in_file:
        in_file.readline()  # Consumes first header line
        for line in in_file:
            parts = line.strip().split("\t")
            start_date = datetime.datetime.strptime(parts[1], "%d/%m/%Y").date()
            projects.append(Project(parts[0], start_date, int(parts[2]), float(parts[3]), int(parts[4])))
    print(f"Loaded {len(projects)} projects from {filename}")


def save_projects(filename, projects):
    """Save projects to filename seperated by \t character."""
    with open(filename, "w") as out_file:
        # Print header line.
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)
        for project in projects:
            line = "\t".join(str(part) for part in project)
            print(line, file=out_file)
    print(f"Saved {len(projects)} projects to {filename}")


def get_valid_string(prompt):
    """Get a non-empty string from user."""
    string = input(prompt)
    while string == "":
        print("Input can not be blank")
        string = input(prompt)
    return string


def get_valid_number(prompt):
    """Get valid integer greater or equal to 0 from user."""
    is_valid_number = False
    while not is_valid_number:
        try:
            number = int(input(prompt))
            if number < 0:
                print("Number must be >= 0")
            else:
                is_valid_number = True
        except ValueError:
            print("Invalid input - please enter a valid number")
    return number  # No risk of being referenced before assignment


main()
