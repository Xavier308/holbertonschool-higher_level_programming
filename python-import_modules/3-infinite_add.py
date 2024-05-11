#!/usr/bin/python3
import sys


def main():
    total = 0
    # Start from 1 to skip the script's name in sys.argv[0]
    for arg in sys.argv[1:]:
        # Convert each argument to an integer and add to total
        total += int(arg)
    print(total)


if __name__ == "__main__":
    main()
