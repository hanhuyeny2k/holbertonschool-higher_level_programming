# Python - Everything Is Object

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
### .txt Answer Files
* Only one line
* No Shebang
* All the files should end with a new line

## Compilation
`$ chmod u+x *.py`

`$ ./19-main.py`

`$ wc -l 19-copy_list.py`

## Example
```#!/usr/bin/python3
copy_list = __import__('19-copy_list').copy_list

my_list = [1, 2, 3]
print(my_list)

new_list = copy_list(my_list)

print(my_list)
print(new_list)

print(new_list == my_list)
print(new_list is my_list)

$ ./19-main.py
[1, 2, 3]
[1, 2, 3]
[1, 2, 3]
True
False
$ wc -l 19-copy_list.py 
3 19-copy_list.py
```

## Tasks
* Understand how to use type(), id().
* Understand if the instances point to the same object or not.
* What to expect when print a string, tuple and integer with the same same 
  variable versus different variables.
* Copy a list into another list.
* Write a blog post on mutable, immutable and object. 
