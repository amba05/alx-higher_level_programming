#!/usr/bin/python3
matrix = [
    [1, 2.3, 3, 6],
    [4, 5.2, 6.7],
    [4, 5.2, 6.7],
    [4, 5.2, 6.7, 6]
]


iterable = iter(matrix)
length = len(next(iterable))
# print(length)
# for l in iterable:
#     print(len(l))
# print(len(next(iterable)))

if all(len(l) == length for l in iterable):
    print("The same!")
else:
    print("Not the same")


# for i in range(len(matrix)):
#     print(next(len(x)))

# len1 = len(matrix[0])
# flag = 0
# for row in matrix:
#     if len(row) != len1:
#         flag = 0
#         break
#     else:
#         flag = 1

# if flag:
#     print("Equal")
# else:
#     print("Not equal")

# for i in range(len(matrix)):
#     if len(matrix[i]) == len(matrix[i+1]):
#         print("Yes, Same")
#         break
#     else:
#         print("No, Not the same!")
#         break
