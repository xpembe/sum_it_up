class Calculator:
    """Operation class for simple calculations"""

    def __init__(self, first_number, second_number):
        """Constructor for initializing the two numbers"""
        self.first_number = first_number
        self.second_number = second_number

    def add(self):
        """Returns the summation of two numbers"""
        return self.first_number + self.second_number

    def subtract(self):
        """Returns the difference of two numbers"""
        return self.first_number - self.second_number

    def multiply(self):
        """Returns the product of two numbers"""
        return self.first_number * self.second_number

    def divide(self):
        """Returns the quotient of two numbers"""
        return self.first_number / self.second_number

    def remainder(self):
        """Returns the remainder of two numbers"""
        return self.first_number % self.second_number
