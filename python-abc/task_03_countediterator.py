#!/usr/bin/env python3
"""
Extends Python's built-in iterator to keep a count of the number of items
iterated over.
"""


class CountedIterator:
    """
    Iterator that counts the number of items iterated over.
    """

    def __init__(self, iterable):
        """
        Initialize the iterator and counter.

        Args:
            iterable: An iterable object to iterate over.
        """
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        """
        Return the next item from the iterator and increment the count.

        Raises:
            StopIteration: If there are no more items to iterate.
        """
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise

    def get_count(self):
        """
        Return the number of items that have been iterated over.

        Returns:
            int: The count of items iterated.
        """
        return self.count
