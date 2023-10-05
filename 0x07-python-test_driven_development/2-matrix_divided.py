#!/usr/bin/python3
""" This divide matrix """


def matrix_divided(matrix, div):
    """ Function for dividing matrix """

    is_valid_matrix = (
            isinstance(matrix, list) and
            all(
                isinstance(row, list)and all(isinstance(num, (int, float)) for num in row)
                for row in matrix
                )
            ) or (
                    isinstance(matrix, list) 
                    and not all(isinstance(row, list) for row in matrix)
                    )

    if not is_valid_matrix:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_size = len(matrix[0])
    if not all(len(row) == row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new = [[round(element / div, 2) for element in row] for row in matrix]
    return new
