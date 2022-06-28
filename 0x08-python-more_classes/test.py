#!/usr/bin/python3
"""
   An Employee class
"""
import datetime


class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@gmail.com'
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
        return self.pay

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    # Alternative constructor
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    def __str__(self):
        return 'My name is {} my email is {} my apply raise is {}.'.format(self.fullname(), self.email, self.apply_raise())


emp1 = Employee("John", "Ken", 12000)
emp2 = Employee("Jay", "Mary", 23000)

emp_str_1 = "Godfrey-james-432200"
emp_str_2 = "Ben-Ken-436200"
emp_str_3 = "John-james-53200"

first, last, pay = emp_str_1.split('-')
emp3 = Employee(first, last, pay)
first, last, pay = emp_str_2.split('-')
emp4 = Employee(first, last, pay)

emp5 = Employee.from_string(emp_str_3)


Employee.set_raise_amt(1.05)
print(Employee.raise_amt)


# is workday
my_date = datetime.date(1996, 11, 1)
print(Employee.is_workday(my_date))


print(emp1.email)
print(emp2.email)
print(emp3.email)
print(emp4.email)
print(emp5.email)
