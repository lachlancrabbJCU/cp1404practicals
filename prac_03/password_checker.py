"""Password checker."""
import string

MIN_LENGTH = 6
MAX_LENGTH = 10
IS_SPECIAL_CHARACTER_REQUIRED = True
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print(f"Your password must be between {MIN_LENGTH} and {MAX_LENGTH} characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if IS_SPECIAL_CHARACTER_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print(f"Your {len(password)}-character password is valid: {password}")


def is_valid_password(password):
    """Determine if the provided password is valid."""
    password_length = len(password)
    if password_length < MIN_LENGTH or password_length > MAX_LENGTH:
        return False
    number_of_lower = 0
    number_of_upper = 0
    number_of_digit = 0
    number_of_special = 0
    for character in password:
        if character.islower():
            number_of_lower += 1
        elif character.isupper():
            number_of_upper += 1
        elif character.isdigit():
            number_of_digit += 1
        elif character in SPECIAL_CHARACTERS:
            number_of_special += 1
        else:  # invalid character
            return False

    if number_of_lower == 0 or number_of_upper == 0 or number_of_digit == 0:
        return False

    if IS_SPECIAL_CHARACTER_REQUIRED and number_of_special == 0:
        return False

    # if we get here (without returning False), then the password must be valid
    return True


main()
