#!/usr/bin/python3

def fizzbuzz():
    """
    Print numbers from 1 to 100 with Fizz for multiples of three,
    Buzz for multiples of five, and FizzBuzz
    for multiples of both three and five.
    """
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")
