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
            pass
        elif choice == "F":
            pass
        elif choice == "A":
            pass
        elif choice == "U":
            pass
        else:
            print("Invalid Choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you for using custom-built project management software.")


def load_projects(filename, projects):
    with open(filename, "r") as in_file:
        in_file.readline()  # Consumes first header line
        for line in in_file:
            parts = line.strip().split("\t")
            projects.append(Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4])))
    print(f"Loaded {len(projects)} projects from {filename}")


main()
