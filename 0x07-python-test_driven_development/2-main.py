#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

try:
    j = matrix_divided([[3, 4, 2.5], [2, 5, 8]], 0)

except Exception as e:
    print(e)

print(matrix_divided(matrix, 3))
print(matrix)
