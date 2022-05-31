#!/usr/bin/python3
for num in range(10):
    for add in range(10):
        if num < add:
            print(str(num) + (str(add)), end="")

            if num != 8 | (num == 8 & add != 9):
                print(", ", end="")

print("\n")
