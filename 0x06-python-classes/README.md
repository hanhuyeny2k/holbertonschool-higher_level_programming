# Classes and Objects
## Prerequisites
* Allowed editors: vi, vim, emacs
* All the files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
* All the files should end with a new line
* The first line of all the files should be exactly #!/usr/bin/python3
* A README.md file, at the root of the folder of the project, is mandatory
* The code should use the PEP 8 style (version 1.7.*)
* All the files must be executable
* The length of the files will be tested using wc
* All the modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
* All the classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
* All the functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
## Compilation
`$ chmod u+x *.py`
`$ ./0-main.py`
## Example
```cat 0-main.py
#!/usr/bin/python3
Square = __import__('0-square').Square

my_square = Square()
print(type(my_square))
print(my_square.__dict__)

./0-main.py
<class '0-square.Square'>
{}```
## Tasks
* Write an empty class Square that defines a square.
* Write a class Square that defines a square by: (based on 0-square.py).
* Write a class Square that defines a square by: (based on 1-square.py).
* Write a class Square that defines a square by: (based on 2-square.py).
* Write a class Square that defines a square by: (based on 3-square.py).
* Write a class Square that defines a square by: (based on 4-square.py).
* Write a class Square that defines a square by: (based on 5-square.py).

