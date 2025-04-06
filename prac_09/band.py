"""
CP1404 Practical - 9
Band class
"""

class Band:
    """Band class that represents a collection of musicians."""
    def __init__(self, name=""):
        """Initialise a Band with a name and empty list of musicians."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of Band."""
        return f"{self.name} ({','.join(str(musician) for musician in self.musicians)})"

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def play(self):
        """Return a string which shows what each musician is playing in the band."""
        return "\n".join(musician.play() for musician in self.musicians)

