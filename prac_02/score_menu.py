"""Score menu to get and display score."""
MENU = """(G)et score
(P)rint result
(S)how stars
(Q)uit"""


def main():
    """Get and display score."""
    print(MENU)
    choice = input(">>> ").upper()
    has_score_set: bool = False
    score = 0
    while choice != "Q":
        # Check if score has been set
        if not has_score_set and choice == ("P" or "S"):
            print("First please give a score")
            score = get_valid_score()
            has_score_set = True
        if choice == "G":
            score = get_valid_score()
            has_score_set = True
        elif choice == "P":
            category = determine_category(score)
            print(f"Score of {score} is {category}")
        elif choice == "S":
            print_stars(score)
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
