#!/usr/bin/python3

def number_keys(a_dictionary):
    # Return the number of keys in the dictionary using the len() function
    return len(a_dictionary)


if __name__ == "__main__":
    # Test the function with a predefined dictionary
    a_dictionary = {'language': "C", 'number': 13, 'track': "Low level"}
    nb_keys = number_keys(a_dictionary)
    print("Number of keys: {:d}".format(nb_keys))
