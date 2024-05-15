#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    # Create a new dictionary with values multiplied by 2 using dictionary
    return {key: value * 2 for key, value in a_dictionary.items()}


if __name__ == "__main__":
    # Import the function to print the dictionary sorted
    from print_sorted_dictionary import print_sorted_dictionary

    # Test dictionary and value multiplication
    a_dictionary = {'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}
    new_dict = multiply_by_2(a_dictionary)
    print_sorted_dictionary(a_dictionary)
    print("--")
    print_sorted_dictionary(new_dict)
