"""CP1404 Prac 09 Silver Service Taxi"""

from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Represent a SilverServiceTaxi object."""
    flagfall = 4.50

    def __init__(self, name: str, fuel: int, fanciness: float):
        """Initialise a SilverServiceTaxi instance."""
        super().__init__(name, fuel)
        self.price_per_km = fanciness * Taxi.price_per_km

    def __str__(self):
        """Return a string like a Taxi but with an added flagfall."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Return the price for the taxi trip."""
        fare = super().get_fare()
        return fare + self.flagfall
