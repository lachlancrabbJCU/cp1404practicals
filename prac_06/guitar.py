""""""
CURRENT_YEAR = 2024
VINTAGE_THRESHOLD = 50


class Guitar:
    """Represent a Guitar object."""
    def __init__(self, name="", year=0, cost=0.0):
        """Initialise a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string of a guitar."""
        return f"{self.name} ({self.year}) : ${self.name:,.2f}"

    def get_age(self):
        """Return age of guitar from CURRENT_YEAR."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Return boolean, True if guitar is older than VINTAGE_THRESHOLD."""
        age = self.get_age()
        return age >= VINTAGE_THRESHOLD
