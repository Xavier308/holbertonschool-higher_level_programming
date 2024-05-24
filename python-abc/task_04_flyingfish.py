#!/usr/bin/env python3
"""
Defines classes to demonstrate multiple inheritance, showcasing a FlyingFish
that inherits behaviors from both Fish and Bird classes.
"""


class Fish:
    """
    Represents basic characteristics of fish.
    """
    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")


class Bird:
    """
    Represents basic characteristics of birds.
    """
    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    Represents a FlyingFish, inheriting from both Fish and Bird.
    """
    def swim(self):
        print("The flying fish is swimming!")

    def fly(self):
        print("The flying fish is soaring!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")
