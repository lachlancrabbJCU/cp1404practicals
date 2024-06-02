"""Password check and display star's."""
MINIMUM_LENGTH = 8


def main():
    """Get password and display stars of passwords length."""
    password = get_valid_password()
    print_stars(password)


def print_stars(password):
    """Print star's length of password."""
    length = len(password)
    print('*' * length)


def get_valid_password():
    """Get password of MINIMUM_LENGTH or greater."""
    password = input("Password: ")
    while len(password) < MINIMUM_LENGTH:
        print(f"Invalid, must be at least {MINIMUM_LENGTH} characters long")
        password = input("Password: ")
    return password


main()
