"""
CP1404 Practical - 9
Taxi Simulator Program
"""

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
    menu_choice = input (">>> ").lower()
    while menu_choice != "q":
        if menu_choice == "c":
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
        elif menu_choice == "d":
            if current_taxi:
                current_taxi.start_fare()
                distance_to_drive = float(input("Drive how far? "))
                current_taxi.drive(distance_to_drive)
                trip_cost = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
                total_bill += trip_cost
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid Option")
        print(f"Bill to date: $ {total_bill:.2f} ")
        print(MENU)
        menu_choice = input(">>> ").lower()

    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now: ")
    display_taxis(taxis)

def display_taxis(taxis):
    """Display all available taxis."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")




if __name__ == '__main__':
    main()