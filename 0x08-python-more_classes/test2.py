#!/usr/bin/python3

class A:
    pass


x = 2
a = A()

if type(a) == A:
    print("Same")
else:
    print("Not same")

print(type(x))
print(type(a))
