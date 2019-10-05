#Python - Test-driven development
##Prerequisites
###Python Scripts
* Allowed editors: vi, vim, emacs
* All the files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
* All the files should end with a new line
* The first line of all the files should be exactly #!/usr/bin/python3
* A README.md file, at the root of the folder of the project, is mandatory
* The code should use the PEP 8 style (version 1.7.*)
* All the files must be executable
* The length of the files will be tested using wc
###Python Test Cases
* Allowed editors: vi, vim, emacs
* All the files should end with a new line
* All the test files should be inside a folder tests
* All the test files should be text files (extension: .txt)
* All the tests should be executed by using this command: python3 -m doctest ./tests/*
* All the modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
* All the functions should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)')
##Compilation
`$ chmod u+x *.py`

`$ ./0-main.py`

`$ python3 -m doctest -v ./tests/0-add_integer.txt | tail -2`

`$ python3 -c 'print(__import__("0-add_integer").__doc__)' | wc -l`

`$ python3 -c 'print(__import__("0-add_integer").add_integer.__doc__)' | wc -l`
##Example
```#!/usr/bin/python3
add_integer = __import__('0-add_integer').add_integer

print(add_integer(1, 2))
print(add_integer(100, -2))
print(add_integer(2))
print(add_integer(100.3, -2))
try:
    print(add_integer(4, "School"))
except Exception as e:
    print(e)
try:
    print(add_integer(None))
except Exception as e:
    print(e)
$ ./0-main.py
3
98
100
98
b must be an integer
a must be an integer
$ python3 -m doctest -v ./tests/0-add_integer.txt | tail -2
9 passed and 0 failed.
Test passed.
$ python3 -c 'print(__import__("0-add_integer").__doc__)' | wc -l
5
$ python3 -c 'print(__import__("0-add_integer").add_integer.__doc__)' | wc -l
3
```

##Tasks
* Write a function that adds 2 integers.
* Write a function that divides all elements of a matrix.
* Write a function that prints My name is <first name last name>.
* Write a function that prints a square with the character #.
* Write a function that prints a text with 2 new line after each of these characters: ., ?, :
* Write a unittests.
