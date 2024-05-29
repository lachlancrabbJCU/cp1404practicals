""""CP1404 sandbox password stars"""


def main():
    minimum_length = 5
    password = get_valid_password(minimum_length)
    print('*' * len(password))


def get_valid_password(minimum_length):
    password = input("Password: ")
    while len(password) < minimum_length:
        print(f"Invalid, must be at least {minimum_length} characters long")
        password = input("Password: ")
    return password


main()
