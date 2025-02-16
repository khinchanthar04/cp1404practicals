"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# Questions
# When will a ValueError occur?
# A ValueError happens when the user enters a non-numeric input or an input that isn't an integer for either the denominator or numerator.

# When will a ZeroDivisionError occur?
# It occurs when we attempt to divide by zero so, it occurs when 0 is entered into the denominator.

# Could you change the code to avoid the possibility of a ZeroDivisionError?
# We could add a few lines of code to check to make sure that zero isn't entered as the denominator before dividing.