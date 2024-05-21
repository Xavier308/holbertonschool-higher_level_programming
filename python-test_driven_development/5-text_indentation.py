#!/usr/bin/python3
"""
This module provides a function called text_indentation that formats text
by inserting two new lines after each '.', '?', and ':'. This helps in
text parsing and presentation, ensuring that each sentence
is clearly separated.
"""


def text_indentation(text):
    """
    Prints text with two new lines after each '.', '?', and ':'.

    Args:
        text (str): The text to print with indentation.

    Raises:
        TypeError: If text is not a string.

    Returns:
        None: This function prints directly to standard output.
    """
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    if text == "":
        print("\n", end="")
        return

    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in ".?:":  # Ensuring ':' is correctly included
            print("\n")
            if i + 1 < len(text) and text[i + 1] == ' ':
                i += 1  # Skip the space after punctuation if it exists
        i += 1


if __name__ == "__main__":
    main()
