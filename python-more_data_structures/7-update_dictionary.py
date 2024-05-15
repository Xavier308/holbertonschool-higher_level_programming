#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    # Update or add the key-value pair in the dictionary
    a_dictionary[key] = value
    return a_dictionary


if __name__ == "__main__":
    # Import the function to print the dictionary sorted
    from print_sorted_dictionary import print_sorted_dictionary

    # Test updating an existing key
    a_dictionary = {'language': "C", 'number': 89, 'track': "Low level"}
    new_dict = update_dictionary(a_dictionary, 'language', "Python")
    print_sorted_dictionary(new_dict)
    print("--")
    print_sorted_dictionary(a_dictionary)

    print("--")
    print("--")

    # Test adding a new key
    new_dict = update_dictionary(a_dictionary, 'city', "San Francisco")
    print_sorted_dictionary(new_dict)
    print("--")
    print_sorted_dictionary(a_dictionary)
