#!/usr/bin/env python3
"""
Extends Python's list class to notify when items are added or removed.
"""


class VerboseList(list):
    """
    A list that prints messages when items are added or removed.
    """

    def append(self, item):
        """
        Append item and print a message.
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, items):
        """
        Extend list by appending elements from the iterable and print
        a message.
        """
        super().extend(items)
        print(f"Extended the list with [{len(items)}] items.")

    def remove(self, item):
        """
        Remove first occurrence of item and print a message.
        """
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """
        Pop item at the index and print a message. Default is last item.
        """
        item = self[index] if self else 'None (list is empty)'
        result = super().pop(index) if self else None
        print(f"Popped [{item}] from the list.")
        return result
