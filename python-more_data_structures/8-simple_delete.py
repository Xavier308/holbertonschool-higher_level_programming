#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    # Attempt to delete the key from the dictionary
    a_dictionary.pop(key, None)
    return a_dictionary


if __name__ == "__main__":
    # Import the function to print the dictionary sorted
    from print_sorted_dictionary import print_sorted_dictionary

    # Test dictionary and key deletion
    a_dictionary = {
        'language': "C",
        'Number': 89,
        'track': "Low",
        'ids': [1, 2, 3]
    }
    new_dict = simple_delete(a_dictionary, 'track')
    print_sorted_dictionary(a_dictionary)
    print("--")
    print_sorted_dictionary(new_dict)

    print("--")
    print("--")

    # Test deleting a non-existent key
    new_dict = simple_delete(a_dictionary, 'c_is_fun')
    print_sorted_dictionary(a_dictionary)
    print("--")
    print_sorted_dictionary(new_dict)
