"""Get and categorise score"""
import random


def main():
    """Get a score and """
    score = float(input("Enter score: "))
    score_category = determine_category(score)
    print(f"Score of {score} is {score_category}")

    # Generate and test function with random score
    random_score = random.randint(0, 100)
    print(f"Score of {random_score} is {determine_category(random_score)}")


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


main()
