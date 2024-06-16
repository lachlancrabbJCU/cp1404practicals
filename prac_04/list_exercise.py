"""List exercise CP1404 Prac 04"""


def main():
    numbers = get_numbers()


def get_numbers():
    numbers = []
    for i in range(5):
        number = int(input("number: "))
        numbers.append(number)
    return numbers


main()
