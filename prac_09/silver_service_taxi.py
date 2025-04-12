"""
CP1404 Practical - 9
SilverServiceTaxi class, derived from Taxi

"""

from prac_09.taxi import Taxi

class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi with higher pricing and flagfall."""

    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        """Initialised a SilverServiceTaxi instance."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness

    def __str__(self):
        """Return a string representation of a SilverServiceTaxi."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Get the current fare."""
        fare = super().get_fare()
        return round(self.flagfall + fare,1)