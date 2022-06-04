# Python - Data Structures: Lists, Tuples

project done during Full Stack Software Engineering studies at __ALX AFRICA SE School__. aims at learning how to use the Data structures such as list, tuples, set and dictionaries in `Python`

## Main.h
* [lists.h](./lists.h): Header file containing prototypes for all functions written in the project.

_Filename_ | _Description_ | _Prototype_
-----------|---------------|------------
[0-print_list_integer.py](./0-print_list_integer.py) | a function that prints all integers of a list. |
[1-element_at.py](./1-element_at.py) | a python script that retrieves an element from a list like in C. |
[2-replace_in_list.py](./2-replace_in_list.py) |a python script that replaces an element of a list at a specific position (like in C).|
[3-print_reversed_list_integer.py](./3-print_reversed_list_integer.py) | a python script that prints all integers of a list, in reverse order. |
[4-new_in_list.py](./4-new_in_list.py) | Python script that replaces an element in a list at a specific position without modifying the original list. |
[5-print_string.py](5-print_string.py) | print 3 times a string stored in the variable str, followed by its first 9 characters. |
[6-concat.py](6-concat.py) | print Welcome to Holberton School! |
[7-edges.py](7-edges.py) | print the first 3, last 2 and middle words of Holberton |
[8-concat_edges.py](8-concat_edges.py) | print object-oriented programming with Python, followed by a new line. |
[9-easter_egg.py](9-easter_egg.py) | a Python script that prints “The Zen of Python”, by TimPeters, followed by a new line. |
[10-check_cycle.c](10-check_cycle.c) | a function in C that checks if a singly linked list has a cycle in it. | `int check_cycle(listint_t *list)`
[100-write.py](100-write.py) | a Python script that prints exactly and that piece of art is useful - Dora Korpar, 2015-10-19, followed by a new line. |
[101-compile](101-compile) | a script that compiles a Python script file. |
[102-magic_calculation.py](102-magic_calculation.py) | python magic file |


## Tasks 🛅

0. **Print intergers in list**
    - [0-print_list_integer.py](./0-print_list_integer.py): python script that prints all integers of a list.


1. **Retrieves element**
    - [1-element_at.py](./1-element_at.py): a python function that retrieves an element from a list like in C..


2. **Replace element**
    - [2-replace_in_list.py](./2-replace_in_list.py): a python script that replaces an element of a list at a specific position (like in C).


3. **Print a list of integers in reverse!**
    - [3-print_reversed_list_integer.py](./3-print_reversed_list_integer.py): Python script that replaces an element in a list at a specific position without modifying the original list.

4. **Replace in a copy**
    - [4-new_in_list.py](./4-new_in_list.py): Python script that prints the float stored in the variable `number` with a precision of two digits.

5. **Print string**
    - [5-print_string.py](5-print_string.py): Python script that prints a string stored in the variable `str` three times, then a new line, then the first nine characters contained in `str`, followed by another new line.
    - Completion of [this source code](https://github.com/holbertonschool/0x00.py/blob/master/5-print_string.py).


6. **Play with strings**
    - [6-concat.py](./6-concat.py): Python script that prints `Welcome to Holberton School!` using the variables `str1 = "Holberton"` and `str2 = "School"`.
    - Completion of [this source code](https://github.com/holbertonschool/0x00.py/blob/master/6-concat.py).


7. **Copy - Cut - Paste**
    - [7-edges.py](7-edges.py): Python script that sets three string variables based on the string contained in the variable `word` as follows:
    - `word_first_3`: Contains the first three letters of the variable `word`.
    - `word_last_2`: Contains the last two letters of the variable `word`.
    - `middle_word`: Contains the value of the variable `word` without the first and last letters.
    - Completion of [this source code](https://github.com/holbertonschool/0x00.py/blob/master/7-edges.py).


8. **Create a new sentence**
    - [8-concat_edges.py](8-concat_edges.py): Python script that prints `object-oriented programming with Python`, followed by a new line without creating new variables or string literals.
    - Completion of [this source code](https://github.com/holbertonschool/0x00.py/blob/master/8-concat_edges.py).


9. **Easter Egg**
    - [9-easter_egg.py](9-easter_egg.py): Python script that prints "The Zen of Python" by Tim Peters, followed by a new line.


10. **Linked list cycle**
    - [10-check_cycle.c](10-check_cycle.c): C function that checks if a linked list contains a cycle.
    - Returns `0` if there is no cycle and `1` if there is.
    - Helper files:
      * [linked_lists.c](./tests/10-linked_lists.c): C functions handling linked lists for testing [10-check_cycle.c](./10-check_cycle.c) (provided by Holberton School).
      * [lists.h](./lists.h): Header file containing definitions and prototypes for all types and functions used in [linked_lists.c](./tests/10-linked_lists.c) and [10-check_cycle.c](./10-check_cycle.c).


11. **Hello, write**
    - [100-write.py](./100-write.py): Python script that prints exactly `and that piece of art is useful - Dora Korpar, 2015-10-19`, followed by a new line to `stderr` using the function `write` from the `sys` module.
    - Exits with a status code of `1`.


12. **Compile**
    - [101-compile](./101-compile): Python script that compiles a Python script file stored in the environment variable `$PYFILE` and saves it to an output file `$PYFILEc` (ex. `export PYFILE=my_main.py` => output filename: `my_main.pyc`).


13. **ByteCode -> Python #1**
    - [102-magic_calculation.py](./102-magic_calculation.py): Python function matching exactly a bytecode provided by Holberton School.
