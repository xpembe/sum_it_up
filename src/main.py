import sys
import prompt as prompt
from calculator import Calculator


def main():
    # Taking the id of operation, making sure it's in range (1-5)
    operation = prompt.choose_operation("Choose operator: ")
    if operation not in range(1, 6):
        print("Error: Invalid operation, choose (1-5).")
        sys.exit()

    try:
        # Taking the numbers from the user for the math operation
        num1 = prompt.number_input("Enter a first number: ")
        num2 = prompt.number_input("Enter a second number: ")

        # Creating an instance (object) for the Calculator class
        calculate = Calculator(num1, num2)

        # Deciding for the operation to be performed
        if operation == 1:
            result = calculate.add()
        if operation == 2:
            result = calculate.subtract()
        if operation == 3:
            result = calculate.multiply()
        if operation == 4:
            result = calculate.divide()
        if operation == 5:
            result = calculate.remainder()

        # Displaying the formatted result
        print("\nResult:", result)

    # Displaying the error message if there was user input errors
    except ValueError:
        print("Error: Enter numbers instead of letters.")


# Ensures the script runs only when executed directly
if __name__ == "__main__":
    main()
