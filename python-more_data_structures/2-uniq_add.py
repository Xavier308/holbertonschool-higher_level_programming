#!/usr/bin/python3

def uniq_add(my_list=[]):
    # Convert the list to a set to remove duplicates and then sum unique elem
    return sum(set(my_list))


if __name__ == "__main__":
    # Test the function with a predefined list
    my_list = [1, 2, 3, 1, 4, 2, 5]
    result = uniq_add(my_list)
    print("Result: {:d}".format(result))
