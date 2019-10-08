# Python - Define a Rectangle Using Classes and Objects

## Prerequisites
* Allowed editors: vi, vim, emacs
* All the files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
* All the files should end with a new line
* The first line of all the files should be exactly #!/usr/bin/python3
* A README.md file, at the root of the folder of the project, is mandatory
* The code should use the PEP 8 style (version 1.7.*)
* All the files must be executable
* The length of the files will be tested using wc

## Compilation
`$ chmod u+x *.py`

`$ ./0-main.py`

## Example
```#!/usr/bin/python3
Rectangle = __import__('0-rectangle').Rectangle

my_rectangle = Rectangle()
print(type(my_rectangle))
print(my_rectangle.__dict__)

$ ./0-main.py
<class '0-rectangle.Rectangle'>
{}
```

## Tasks
* Write an empty class Rectangle that defines a rectangle.
* Write a class Rectangle that defines a rectangle by its width and height.
* Write a class Rectangle that defines a rectangle by its area and perimeter.
* Write a class Rectangle that defines a rectangle by string representation.
* Write a class Rectangle that defines a rectangle by using str() and repr().
* Write a class Rectangle that defines a rectangle by detecting instance deletion.
* Write a class Rectangle that defines a rectangle by how many instances.
* Write a class Rectangle that defines a rectangle by changing representation.
* Write a class Rectangle that defines a rectangle by comparing rectangles.
* Write a class Rectangle that defines a rectangle by turning it into a square. 
