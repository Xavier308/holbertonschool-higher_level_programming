#!/usr/bin/python3
import sys
import os
import importlib.util


def main():
    # the path to the .pyc file
    module_path = "/tmp/hidden_4.pyc"

    # Load the module dynamically
    spec = importlib.util.spec_from_file_location("hidden_4", module_path)
    hidden_4 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(hidden_4)

    # Filter and print the names defined in the module
    names = [name for name in dir(hidden_4) if not name.startswith('__')]
    names.sort()
    for name in names:
        print(name)


if __name__ == "__main__":
    main()
