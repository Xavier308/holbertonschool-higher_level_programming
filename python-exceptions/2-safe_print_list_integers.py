#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            # Check if the current element is an integer
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                count += 1
        except IndexError:
            # Break out of the loop if index is out of range
            break
    print()  # Ensures a newline after finishing printing
    return count


if __name__ == "__main__":
    # Test cases
    my_list = [1, 2, 3, 4, 5]
    nb_print = safe_print_list_integers(my_list, 2)
    print("nb_print: {:d}".format(nb_print))

    my_list = [1, 2, 3, "School", 4, 5, [1, 2, 3]]
    nb_print = safe_print_list_integers(my_list, 7)
    print("nb_print: {:d}".format(nb_print))

    nb_print = safe_print_list_integers(my_list, 9)
    print("nb_print: {:d}".format(nb_print))
