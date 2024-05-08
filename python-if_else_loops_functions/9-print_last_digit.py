#!/usr/bin/python3

def print_last_digit(number):
    """
    Print the last digit of a number and return its value.

    Args:
        number: An integer.

    Returns:
        The value of the last digit.
    """
    # Get the absolute value of the number to handle negative numbers
    number = abs(number)
    # Get the last digit of the number by taking its modulo 10
    last_digit = number % 10
    # Print the last digit without a newline
    print(last_digit, end="")
    # Return the value of the last digit
    return last_digit
