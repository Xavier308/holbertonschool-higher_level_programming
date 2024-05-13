#!/usr/bin/python3

def multiple_returns(sentence):
    """
    Returns a tuple with the length of the string sentence
    and its first character.
    If sentence is empty, the first character is None.
    """
    if sentence:
        return (len(sentence), sentence[0])
    else:
        return (0, None)
