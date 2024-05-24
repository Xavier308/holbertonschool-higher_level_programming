#!/usr/bin/env python3
"""
Defines mixin classes to add swimming and flying behaviors, and a Dragon class
that demonstrates the use of these mixins.
"""


class SwimMixin:
    """
    Mixin class providing a swim method.
    """
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """
    Mixin class providing a fly method.
    """
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    A class representing a mythical dragon that can swim and fly.
    Mixes in swimming and flying capabilities.
    """
    def roar(self):
        print("The dragon roars!")
