#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                count += 1
        except IndexError:
            break
    print()  # Ensure newline after printing
    return count


if __name__ == "__main__":
    # Test cases
    my_list = [1, 2, 3, 4, 5]
    nb_print = safe_print_list_integers(my_list, 2)
    print("nb_print: {:d}".format(nb_print))  # Expected output: 2

    my_list = [1, 2, 3, "School", 4, 5, [1, 2, 3]]
    nb_print = safe_print_list_integers(my_list, len(my_list))
    print("nb_print: {:d}".format(nb_print))  # Expected output: 5

    # This should handle the IndexError properly by breaking the loop
    nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
    print("nb_print: {:d}".format(nb_print))  # Expected output: 5
