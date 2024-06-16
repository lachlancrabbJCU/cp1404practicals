"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = load_data()
    print_subject_details(data)


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    data = []
    input_file = open(FILENAME)
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        data.append(parts)
        print(parts)  # See if that worked
        print("----------")
    input_file.close()
    return data


def print_subject_details(data):
    name_max_length = max((len(parts[1]) for parts in data))  # find max width of name
    students_max_length = max((len(str(parts[2])) for parts in data))  # find max width of number of students
    for parts in data:
        print(f"{parts[0]} is taught by {parts[1]:{name_max_length}} and has {parts[2]:{students_max_length}} students")


main()
