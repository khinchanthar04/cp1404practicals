"""
CP1404 Practical - 9
Taxi Simulator Program
"""

from prac_09.car import Car
from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "Q)uit, C)hoose taxi, D)rive"

def main():
    """Write a taxi simulator program that uses Taxi and SilverServiceTaxi classes."""
    total_bill = 0
    current_taxi = None
    taxis = [Taxi("Prius", 100),
             SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's drive!")
    print(MENU)
    menu_choice = input (">>> ").upper()
    while menu_choice != "Q":
        if menu_choice == "C":
            print("Available Taxis: ")
            display_taxis(taxis)
            taxi_choice = int(input("Choose taxi: "))

            try:
                taxi_choice = int(taxi_choice)
                if 0<= taxi_choice < len(taxis):
                    current_taxi = taxis[taxi_choice]
                else:
                    print("Invalid taxi choice")
            except ValueError and IndexError:
                print("Invalid Input!")
        elif menu_choice == "D":
            print("Drive")
        else:
            print("Invalid Option")
        print("Bill to date: $ . . . ")
        print(MENU)
        menu_choice = input(">>> ").upper()

    print(f"Total trip cost:")
    print("Taxis are now: ")

def display_taxis(taxis):
    """Display all available taxis."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


if __name__ == '__main__':
    main()