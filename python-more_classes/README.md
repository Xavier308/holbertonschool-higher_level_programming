# Python - More Classes and Objects

This repository contains the exercises for the "Python - More Classes and Objects" project at Holberton School. This project focuses on deepening understanding of object-oriented programming (OOP) in Python, covering attributes, methods, special methods (`__str__`, `__repr__`), and more.

## Implemented by
Xavier J. Cruz (based on content by Guillaum)

### Resources
- [Object Oriented Programming](https://python.swaroopch.com/oop.html)
- [Class and Instance Attributes](https://www.python-course.eu/python3_class_and_instance_attributes.php)
- [classmethods and staticmethods](https://realpython.com/instance-class-and-static-methods-demystified/)
- [Properties vs. Getters and Setters](https://www.python-course.eu/python3_properties.php)
- [str vs repr](https://www.geeksforgeeks.org/str-vs-repr-in-python/)

### Learning Objectives

- Why Python programming is awesome
- What is OOP, including concepts like classes, objects, instance attributes, methods, etc.
- Differences between class attributes and instance attributes
- What are and how to use public, protected, and private attributes
- The special `__init__`, `__str__`, and `__repr__` methods
- Data Abstraction, Data Encapsulation, and Information Hiding
- The Pythonic way to write getters and setters
- How to dynamically create attributes for existing instances
- Much more about OOP principles in Python

### Requirements
- All files are interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- Code should use the pycodestyle (version 2.7.*)
- All files must be executable
- The length of files will be tested using `wc`

### Tasks
#### 0. Simple rectangle
- Implement an empty class named Rectangle that defines a rectangle.

#### 1. Real Definition of a Rectangle
- Define the Rectangle with private attributes width and height and include property setters and getters to validate type and enforce non-negative values.

#### 2. Area and Perimeter
- Extend the Rectangle class to calculate and return the area and perimeter. Implement zero-checks for width or height.

#### 3. String Representation
- Implement the __str__ method in the Rectangle class to provide a string representation using the # character.

#### 4. Eval is Magic
- Enhance the Rectangle class by adding the __repr__ method to allow instance recreation using eval().

#### 5. Detect instance deletion
- Implement a destructor in the Rectangle class to print a message when an instance is deleted.

#### 6. How Many Instances
- Track the number of Rectangle instances with a class attribute that increments/decrements with each instance creation/deletion.

#### 7. Change Representation
- Modify the Rectangle class to allow changing the symbol used in the string representation dynamically.

#### 8. Compare rectangles
- Add a static method to the Rectangle class to compare the area of two rectangles and return the bigger or the first if they are equal.

#### 9. A Square is a Rectangle
- Implement a class method in the Rectangle class that allows creating a square (a rectangle with equal width and height).

