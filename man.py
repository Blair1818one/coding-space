# This program calculates the factorial of a given number using a loop.

# Function to calculate factorial using a loop
def calculate_factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

# Main program
number = int(input("Enter a number: "))
if number >= 0:
    result = calculate_factorial(number)
    print(f"{number}! = {result}")
else:
    print("Factorial is not defined for negative numbers.")
