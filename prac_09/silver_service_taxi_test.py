"""
CP1404 Practical - 9
SilverServiceTaxi class Tests

"""

from prac_09.silver_service_taxi import SilverServiceTaxi

def main():
    """Test for SilverServiceTaxi class."""

    hummer = SilverServiceTaxi("Hummer", 200, 2)
    hummer.start_fare()
    hummer.drive(18)
    print(hummer)
    fare = hummer.get_fare()
    print(f"Fare: ${fare}")

    assert abs(fare - 48.78)< 0.01, f"Expected $48.80 but got ${fare:.2f}"
if __name__ == '__main__':
    main()