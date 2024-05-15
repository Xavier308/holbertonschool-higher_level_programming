#!/usr/bin/python3

def common_elements(set_1, set_2):
    # Return the intersection of two sets using the intersection method
    return set_1.intersection(set_2)


if __name__ == "__main__":
    # Test the function with two predefined sets
    set_1 = {"Python", "C", "Javascript"}
    set_2 = {"Bash", "C", "Ruby", "Perl"}
    c_set = common_elements(set_1, set_2)
    print(sorted(list(c_set)))
