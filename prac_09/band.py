"""CP1404 Prac 09 Band."""


class Band:
    """Represent a Band object."""

    def __init__(self, name):
        """Initialise a Band instance."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of a Band."""
        return f"{self.name} ({self.musicians})"

    def add(self, musician):
        """Add a musician to band."""
        self.musicians.append(musician)

    def play(self):
        """Return a string showing the instrument playing their first (or no) instrument."""
        for musician in self.musicians:
            print(musician.play())
