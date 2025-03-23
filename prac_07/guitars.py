"""
CP1404 Practical - 7
Guitar Program
"""
from prac_07.guitar import Guitar


def main():
    """Guitar program, using Guitar class."""
    guitars = load_guitars()

    print("My guitars!")
    name = input("Name: ")

    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitars.append(Guitar(name, year, cost))
        print(f"{name} ({year}) : ${cost:.2f} added.")
        name = input("Name: ")

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    if guitars:
        print("These are my guitars:")
        for i, guitar in enumerate(guitars, 1):
            vintage_string = ""
            if guitar.is_vintage():
                vintage_string = " (vintage)"

            print(f"Guitar {i}: {guitar.name} ({guitar.year}), worth ${guitar.cost:.2f}{vintage_string}")
    else:
        print("No guitars :( Quick, go and buy one!")

def load_guitars():
    """Load guitars from the CSV file."""
    guitars = []
    with open("guitars.csv", "r") as file:
        for line in file:
            name, year, cost = line.strip().split(',')
            guitars.append(Guitar(name,int(year),float(cost)))
    return guitars


main()
