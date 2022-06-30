#!/usr/bin/python3
"""
    Divides all elements of a matrix with a given divisor.
"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix
        Args:
            matrix (list): matrix of int/float lists
            div (int): divisor for matrix item
        Returns:
            A new list with result
    """
    if not isinstance(div, (int, float)) or div is None:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(matrix, list):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        len_of_first_row = len(matrix[0])
        if len(row) != len_of_first_row:
            raise TypeError("Each row of the matrix must have the same size")

        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats")

        # new_list = []
        # res = list(map(lambda item: round(item / div, 2), row))
        # new_list.append(res)

    # return new_list
    return [list(map(lambda item: round(item / div, 2), row)) for row in matrix]
