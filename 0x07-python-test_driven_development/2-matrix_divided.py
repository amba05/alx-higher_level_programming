#!/usr/bin/python3
def matrix_divided(matrix, div):
    if type(matrix) != list:
        raise TypeError('matrix must be a matrix (list of lists)' /
                        'of integers/floats')

    for i in matrix:
        if type(i) != list:
            raise TypeError('matrix must be a matrix (list of lists)' /
                            'of integers/floats')
        for j in i:
            if type(j) not in [int, float]:
                raise TypeError('matrix must be a matrix (list of lists)'
                                'of integers/floats')

    len_1 = len(matrix[0])
    for j in matrix:
        if len_1 != len(j):
            raise TypeError('Each row of the matrix must have the same size')

    if type(div) not in [int, float]:
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    ans = []
    val = 0

    for a in matrix:
        arr = []

        for b in a:
            val = b / div
            arr.append(round(val, 2))
        ans.append(arr)

    return ans
