"""Some functions for prompting user"""


def number_input(prompt):
    """Prompting user for number inputs"""
    return int(input(prompt))


def choose_operation(prompt):
    """Prompting user for operation to be performed"""
    template = """
        1. Addition
        2. Subtraction
        3. Multiplication
        4. Division
        5. Remainder
        """
    print(template)
    return int(input(prompt))
