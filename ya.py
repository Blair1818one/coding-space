# Project Title: Factorial Calculator

# This program calculates the factorial of a non-negative integer.
# Example: 5! = 5 * 4 * 3 * 2 * 1 = 120.
# It uses a 'for' loop for the calculation.

def calculate_factorial():
    """
    Calculates and prints the factorial of a user-provided non-negative integer.
    Includes basic input validation.
    """
    while True: # Loop to ensure valid input
        try:
            num = int(input("Enter a non-negative integer for factorial: "))

            if num < 0:
                print("Error: Factorial not defined for negative numbers. Try again.")
                continue
            else:
                break # Exit loop if input is valid
        except ValueError:
            print("Error: Invalid input. Please enter a whole number.")

    factorial = 1 # Initialize factorial

    if num == 0:
        print(f"The factorial of {num} is 1")
    else:
        # Calculate factorial using a loop
        for i in range(1, num + 1):
            factorial *= i

        print(f"The factorial of {num} is {factorial}")

# Run the program
if __name__ == "__main__":
    calculate_factorial()