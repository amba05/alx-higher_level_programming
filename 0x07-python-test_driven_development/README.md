# Python - Test-driven development

## Important codes
- Checking availability of documentation for modules
	` python3 -c 'print(__import__("*module_name*").__doc__)' `

-  checking line count for modules documentation
	`python3 -c 'print(__import__("*module_name*").__doc__)' | wc -l
5`

- Checking availability of documentation for functions
        ` python3 -c 'print(__import__("*module_name*").*function_name*.__doc__)' `

-  checking line count for functions documentation
        `python3 -c 'print(__import__("*module_name*").*function_name*.__doc__)' | wc -l
5`

EXAMPLE:
	`python3 -c 'print(__import__("0-add_integer").__doc__)' | wc -l
5`

	`python3 -c 'print(__import__("0-add_integer").add_integer.__doc__)' | wc -l`


- Run doc test for examples in documentions
	`python3 -m doctest -v file_name`

*EXAMPLE*
	`python3 -m doctest -v ./tests/0-add_integer.txt | tail -2`


**NB** 
## Doc_test module
	- The simplest way to write doctest is by writing the test cases inside the module and attaching this;
		`if __name__ == "__main__":`
			`import doctest`
			`doctest.testmod()`
	- Then the module can be tested with either;
		`python3 module_name`  --- (non-detailed report, except failed test cases)  **OR**
		`python3 module_name -v`   --- (detailed report of all test cases)

## Doc_test file
	- Another way to do it is by creating a file with test cases to be tested, it is most preffered method
	  in python as it avoids cluttering of code with doctests.

	- it is done by importing doctest in the python_file(code) and attaching the supposed file with the test cases;
		**open file.py**
		`import doctest`
		`doctest.testfile("file.txt")`

	- Then create the test_file(containing test cases) then import the test file and write the test cases.
		** open file.txt **
		`>>> from file import test_function`
		`>>> add(6, 5)`
		`11`


