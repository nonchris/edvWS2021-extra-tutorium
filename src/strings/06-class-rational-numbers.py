# a basic example class to give an idea of how classes work
# the basic examples are with cars or persons
# I'd like to show of a rather advanced 'useful' example

import numpy as np


class RationalNumber:
    def __init__(self, numerator, denominator):
        """
        __init()__ is the standard function every class needs to be functional
        here's that basic stuff like preparing needed data
        init() can also call other class functions
        """
        # counter and denominator must be integers
        self.numerator = numerator
        self.denominator = denominator

        self.value = numerator / denominator

        # self.simplify()  # could be called from here to simplify automatically on init()

    def __repr__(self):
        """Overwrites the standard function called, when someone tries to use print() on the class"""
        return f"{self.numerator}/{self.denominator}"

    def simplify(self):
        # calculating greatest common divisor
        gcd = np.gcd(self.numerator, self.denominator)
        self.numerator = int(self.numerator / gcd)
        self.denominator = int(self.denominator / gcd)

    def multiply(self, factor: int):
        """Multiply the number with an integer"""
        self.numerator *= factor

    def multiply_with_rational(self, num):
        """Multiply two rational numbers"""
        self.numerator = self.numerator * num.numerator
        self.denominator = self.denominator * num.denominator

    def to_string(self):
        """Class functions can have return values, sure!"""
        return f"{self.denominator} / {self.numerator}"


if __name__ == "__main__":
    """
    This statement checks if this file was executed as itself and only then runs that code below
    If this file would be imported by an other file this could would not be executed
    Which is useful because you want to import only functions and classes and not to execute some random demo code
    """
    # create an object from our class
    rational_number = RationalNumber(2, 4)

    print(rational_number)  # print number (calls __repr__())
    print()

    #  getting value from class and printing it
    #  notice any parallels to e.g. np.pi ?
    value = rational_number.value
    print(value)
    print()

    # calling class function simplify() on our object
    rational_number.simplify()
    print(rational_number)
    print()

    # multiplying it with 3
    rational_number.multiply(3)
    print(rational_number)
    print()

    # creating second object
    sencond_number = RationalNumber(4, 5)

    # calling multiply:with_rational() on our first number
    # -> values of the first number will change, the second one stays untouched
    # notice how we don't need any new variables to save our new results?
    # there are no returns, it all happens inside this object!
    rational_number.multiply_with_rational(sencond_number)
    print("First number:", rational_number)

    # but they can have return values!
    number2_as_string = sencond_number.to_string()
    print("Second number:", number2_as_string)

    # we can also modify values inside a class
    rational_number.denominator = 42
    print("Modified first number:", rational_number)

