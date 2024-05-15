#!/usr/bin/python3
def safe_print_division(a, b):
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result


if __name__ == "__main__":
    # Test cases
    a = 12
    b = 2
    result = safe_print_division(a, b)
    print("{:d} / {:d} = {}".format(a, b, result))

    a = 12
    b = 0
    result = safe_print_division(a, b)
    print("{:d} / {:d} = {}".format(a, b, result))
