"""mod doc"""
MENU = """(G)et score
(P)rint result
(S)how stars
(Q)uit"""


def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            category = determine_category(score)
            print(f"Score of {score} is {category}")
        elif choice == "S":
            print_stars(score)  # Print score number of stars
        else:
            print("Invalid Choice.")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you for using the score menu\nGood Bye")


def get_valid_score() -> float:
    """Get a valid score between low and high"""
    score = float(input("Score: "))
    while score < 0 or score > 100:
        print(f"invalid score, must be between 0 and 100 inclusive")
        score = float(input("Score: "))
    return score


def determine_category(score: float) -> str:
    """Determine score category based on score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score < 50:
        return "Bad"
    elif score < 90:
        return "Passable"
    else:
        return "Excellent"


def print_stars(length):
    """Print number of stars equal to length"""
    print('*' * int(length))


main()
