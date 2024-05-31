"""mod doc"""
MENU = """menu:"""


def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            pass
        elif choice == "P":
            pass
        elif choice == "S":
            pass
        else:
            print("Invalid Choice.")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you for using the score menu\nGood Bye")


main()
