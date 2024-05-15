#!/usr/bin/python3

def search_replace(my_list, search, replace):
    # Using list comprehension to create a new list where
    # each element is replaced if it matches the 'search' value
    return [replace if x == search else x for x in my_list]


if __name__ == "__main__":
    # Test the function with a predefined list
    my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
    new_list = search_replace(my_list, 2, 89)

    print(new_list)
    print(my_list)  # The original list remains unchanged
