#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    # Return the symmetric difference of two sets
    return set_1.symmetric_difference(set_2)


if __name__ == "__main__":
    # Test the function with two predefined sets
    set_1 = {"Python", "C", "Javascript"}
    set_2 = {"Bash", "C", "Ruby", "Perl"}
    od_set = only_diff_elements(set_1, set_2)
    print(sorted(list(od_set)))
