 #!/usr/bin/python3
def uppercase(s):
    """
    Print a string in uppercase followed by a new line.

    Args:
        s: A string.
    """
    for char in s:
        # Check if the character is lowercase
        if ord('a') <= ord(char) <= ord('z'):
            # Convert lowercase character to uppercase
            uppercase_char = chr(ord(char) - 32)
        else:
            uppercase_char = char
        # Print the uppercase character without a newline
        print(uppercase_char, end="")
    # Print a newline after printing the uppercase string
    print()
