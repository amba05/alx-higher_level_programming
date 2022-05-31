#!/usr/bin/python3
def fizzbuzz():
    for elem in range(1, 101):
        if (elem % 3 == 0) & (elem % 5 == 0):
            print("FizzBuzz", end=" ")
        elif elem % 5 == 0:
            print("Buzz ", end=" ")
        elif elem % 3 == 0:
            print("Fizz ", end=" ")
        else:
            print(elem, end=" ")
