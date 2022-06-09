#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    add = []
    for i in matrix:
        ans = map(lambda x: x * x, i)
        add.append(list(ans))
    return add


