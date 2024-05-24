#!/usr/bin/env python3
"""
This module defines an abstract class, Animal, and two of its subclasses,
Dog and Cat.
The Animal class serves as a blueprint for creating animals with distinct
sound behaviors.
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    A class used to represent an Animal.

    This is an abstract class that cannot be instantiated and requires
    subclasses to implement the sound method.

    Methods
    -------
    sound()
        Abstract method that should be implemented by subclasses to return
        the animal's sound.
    """
    @abstractmethod
    def sound(self):
        """
        Represents the sound made by the animal.

        This method is abstract and must be overridden in subclasses.
        """
        pass


class Dog(Animal):
    """
    A class used to represent a Dog, subclass of Animal.

    Methods
    -------
    sound()
        Returns the sound 'Bark' typical of dogs.
    """
    def sound(self):
        """
        Return the sound made by the dog.
        """
        return "Bark"


class Cat(Animal):
    """
    A class used to represent a Cat, subclass of Animal.

    Methods
    -------
    sound()
        Returns the sound 'Meow' typical of cats.
    """
    def sound(self):
        """
        Return the sound made by the cat.
        """
        return "Meow"
