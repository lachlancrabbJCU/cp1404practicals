class ProgrammingLanguage:

    def __init__(self, name, typing, is_reflection, year):
        """Initialise a ProgrammingLanguage instance."""
        self.name = name
        self.typing = typing
        self.is_reflection = is_reflection
        self.year = year

    def __str__(self):
        """Return string of a ProgrammingLanguage instance."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.is_reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Return boolean based on dynamic typing."""
        return self.typing == "Dynamic"
