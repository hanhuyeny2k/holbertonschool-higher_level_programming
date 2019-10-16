# Python - Inheritance

## Prerequisites
### Python Scripts
* Allowed editors: vi, vim, emacs
* All the files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
* All the files should end with a new line
* The first line of all the files should be exactly #!/usr/bin/python3
* A README.md file, at the root of the folder of the project, is mandatory
* The code should use the PEP 8 style (version 1.7.*)
* All the files must be executable
* The length of the files will be tested using wc
### Python Test Cases
* Allowed editors: vi, vim, emacs
* All the files should end with a new line
* All the test files should be inside a folder tests
* All the test files should be text files (extension: .txt)
* All the tests should be executed by using this command: python3 -m doctest ./tests/*
* All the modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
* All the classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
* All the functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')

## Compilation
`$ chmod u+x *.py`

`$ ./1-main.py`

## Example
```$ cat 1-main.py
#!/usr/bin/python3
MyList = __import__('1-my_list').MyList

my_list = MyList()
my_list.append(1)
my_list.append(4)
my_list.append(2)
my_list.append(3)
my_list.append(5)
print(my_list)
my_list.print_sorted()
print(my_list)

$ ./1-main.py
[1, 4, 2, 3, 5]
[1, 2, 3, 4, 5]
[1, 4, 2, 3, 5]
```

## Tasks
* Write a function that returns the list of available attributes and methods of an object.
* Write a class MyList that inherits from list.
* Write a function that returns True if the object is exactly an instance of the specified class ; otherwise False.
* Write a function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False.
* Write a function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False.
* Write an empty class BaseGeometry.
* Write a class BaseGeometry (based on 5-base_geometry.py).
* Write a class BaseGeometry (based on 6-base_geometry.py).
* Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py).
* Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py). (task based on 8-rectangle.py)
* Write a class Square that inherits from Rectangle (9-rectangle.py).
* Write a class Square that inherits from Rectangle (9-rectangle.py). (task based on 10-square.py).

