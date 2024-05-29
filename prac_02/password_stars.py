""""CP1404 sandbox password stars"""


def main():
    minimum_length = 8
    password = get_valid_password(minimum_length)
    print_stars(password)


def print_stars(password):
    """Print *'s length of password."""
    length = len(password)
    print('*' * length)


def get_valid_password(minimum_length):
    """Get password of minimum length or greater."""
    password = input("Password: ")
    while len(password) < minimum_length:
        print(f"Invalid, must be at least {minimum_length} characters long")
        password = input("Password: ")
    return password


main()
