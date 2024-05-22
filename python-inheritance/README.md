# Python - Inheritance

This repository contains a series of tasks related to the concept of inheritance in Python programming. These tasks are designed to demonstrate the use and capabilities of inheritance, including basic and multiple inheritance patterns.

## Implemented by
Xavier J. Cruz (based on content by Guillaume)


## Resources
- [Inheritance](https://docs.python.org/3/tutorial/classes.html#inheritance)
- [Multiple inheritance](https://docs.python.org/3/tutorial/classes.html#multiple-inheritance)
- [Inheritance in Python](https://realpython.com/inheritance-composition-python/)
- [Learn to Program 10: Inheritance Magic Methods](https://www.youtube.com/watch?v=d8kCdLCi6Lk)

## Learning Objectives

- What is a superclass, baseclass or parentclass
- What is a subclass
- How to list all attributes and methods of a class or instance
- When an instance can have new attributes
- How to inherit class from another
- How to define a class with multiple base classes
- What is the default class every class inherit from
- How to override a method or attribute inherited from the base class
- Which attributes or methods are available by heritage to subclasses
- What is the purpose of inheritance
- When and how to use isinstance, issubclass, type and super built-in functions

## Requirements
### Python Scripts
- **Environment**: Ubuntu 20.04 LTS using Python 3.8.5
- **Style**: pycodestyle (version 2.7.*)
- **Execution**: All files must be executable and begin with `#!/usr/bin/python3`
- **Documentation**: All modules, classes, and functions must include detailed docstrings.

### Python Test Cases
- **Test files location**: All test files should be inside a `tests` folder.
- **Test file type**: All test files should be text files (extension: `.txt`).
- **Execution command**: `python3 -m doctest ./tests/*`

## Tasks
0. **Lookup** - Function that returns a list of available attributes and methods of an object.
1. **My List** - Class `MyList` that inherits from `list`, with a method to print the list sorted.
2. **Exact same object** - Function to check if an object is exactly an instance of a specified class.
3. **Same class or inherit from** - Function to check if an object is an instance of, or inherits from, a specified class.
4. **Only sub class of** - Function to check if an object is an instance of a class that inherited from a specified class.
5. **Geometry module** - Empty class `BaseGeometry`.
6. **Improve Geometry** - Class `BaseGeometry` with public instance method `area()` and validator `integer_validator`.
7. **Integer validator** - `BaseGeometry` class with added integer validation.
8. **Rectangle** - Class `Rectangle` that inherits from `BaseGeometry`.
9. **Full rectangle** - Improved `Rectangle` class with print functionality.
10. **Square #1** - Class `Square` that inherits from `Rectangle`.
11. **Square #2** - Improved `Square` class with custom print functionality.

## Documentation Guidelines
- Avoid using the words `import` or `from` inside comments to prevent documentation
