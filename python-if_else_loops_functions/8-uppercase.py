#!/usr/bin/python3

def uppercase(s):
    """
    Print a string in uppercase followed by a new line.
    
    Args:
        s: A string.
    """
    result = ""  # Initialize an empty string to store the uppercase string
    for char in s:
        # Check if the character is lowercase
        if ord('a') <= ord(char) <= ord('z'):
            # Convert lowercase character to uppercase
            uppercase_char = chr(ord(char) - 32)
        else:
            uppercase_char = char
        # Append the uppercase character to the result string
        result += uppercase_char
    # Print the uppercase string followed by a newline using format
    print("{}".format(result))
