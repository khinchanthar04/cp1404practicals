"""
CP1404 Practical 4
List Exercises
"""
# 1. Numbers

numbers = []
COUNT = 5
for i in range(COUNT):
    number = int(input("Enter number: "))
    numbers.append(number)

average = sum(numbers)/len(numbers)

print(f"The first number is {numbers[0]}.")
print(f"The last number is {numbers[-1]}.")
print(f"The smallest number is {min(numbers)}.")
print(f"The largest number is {max(numbers)}.")
print(f"The average of the number is {average}")

