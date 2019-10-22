# Python - Python - Input/Output

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

`$ ./0-main.py`

## Example
```$ cat 0-main.py
#!/usr/bin/python3
read_file = __import__('0-read_file').read_file

read_file("my_file_0.txt")

$ cat my_file_0.txt
Holberton School offers a truly innovative approach to education:
focus on building reliable applications and scalable systems, take on real-world challenges, collaborate with your peers. 

A school every software engineer would have dreamt of!
$ ./0-main.py
Holberton School offers a truly innovative approach to education:
focus on building reliable applications and scalable systems, take on real-world challenges, collaborate with your peers. 

A school every software engineer would have dreamt of!
```

## Tasks
* Write a function that reads a text file (UTF8) and prints it to stdout.
* Write a function that returns the number of lines of a text file.
* Write a function that reads n lines of a text file (UTF8) and prints it to stdout.
* Write a function that writes a string to a text file (UTF8) and returns the number of characters written.
* Write a function that appends a string at the end of a text file (UTF8) and returns the number of characters added.
* Write a function that returns the JSON representation of an object (string).
* Write a function that returns an object (Python data structure) represented by a JSON string.
* Write a function that writes an Object to a text file, using a JSON representation.
* Write a function that creates an Object from a JSON file.
* Write a script that adds all arguments to a Python list, and then save them to a file.
* Write a function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object.
* Write a class Student that defines a student.
* Create a function def pascal_triangle(n): that returns a list of lists of integers representing the Pascals triangle of n.
