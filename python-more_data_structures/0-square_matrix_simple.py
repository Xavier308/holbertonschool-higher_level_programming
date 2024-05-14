#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    # This function uses list comprehension to create a new matrix
    # Each element is squared using the expression x**2
    return [[x**2 for x in row] for row in matrix]


if __name__ == "__main__":
    # Test the function with a predefined matrix
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    new_matrix = square_matrix_simple(matrix)
    print(new_matrix)
    print(matrix)  # The original matrix remains unchanged
