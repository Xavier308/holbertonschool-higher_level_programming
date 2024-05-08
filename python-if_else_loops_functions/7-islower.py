#!/usr/bin/python3
def islower(c):
    """
    Check if a character is lowercase.

    Args:
        c: A character (string of length 1).

    Returns:
        True if c is lowercase, False otherwise.
    """
    # Check the ASCII value of c
    return ord('a') <= ord(c) <= ord('z')
