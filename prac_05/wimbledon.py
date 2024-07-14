"""
Wimbledon
Estimate: 25 minutes
Actual: 50 minutes
"""


def main():
    """Read file of Wimbledon championships and display the winning players and countries."""
    championships = retrieve_data()
    display_champions(championships)
    print()
    display_winning_countries(championships)


def display_winning_countries(championships):
    """Display countries that have one wimbledon."""
    winning_countries = set((championship[1] for championship in championships))
    print(f"These {len(winning_countries)} countries have won Wimbledon:")
    print(", ".join(sorted(list(winning_countries))))


def display_champions(championships):
    """Display champions along with the number of times they have won."""
    name_to_wins = {}
    for championship in championships:
        try:
            name_to_wins[championship[2]] += 1
        except KeyError:
            name_to_wins[championship[2]] = 1

    print("Wimbledon Champions:")
    for name, number_of_wins in name_to_wins.items():
        print(f"{name} {number_of_wins}")


def retrieve_data():
    """Load data from a CSV file to a list of lists."""
    data = []
    with open("wimbledon.csv", "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # remove header from data
        for line in in_file:
            data.append(line.strip().split(","))
    return data


main()
