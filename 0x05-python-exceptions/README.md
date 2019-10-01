### Python - Exceptions
## Prerequisites
* Allowed editors: vi, vim, emacs
* All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
* All your files should end with a new line
* The first line of all your files should be exactly #!/usr/bin/python3
* A README.md file, at the root of the folder of the project, is mandatory
* Your code should use the PEP 8 style (version 1.7.*)
* All your files must be executable
* The length of your files will be tested using wc
## Compilation
$ chmod u+x *.py
## Usage
$ ./1-main.py
## Example
cat 1-main.py
#!/usr/bin/python3
safe_print_integer = __import__('1-safe_print_integer').safe_print_integer

value = 89
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = -89
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = "Holberton"
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))

./1-main.py
89
-89
Holberton is not an integer
## Tasks
* Write a function that prints x elements of a list.
* Write a function that prints an integer with "{:d}".format().
* Write a function that prints the first x elements of a list and only integers.
* Write a function that divides 2 integers and prints the result.
* Write a function that divides element by element 2 lists.
* Write a function that raises a type exception.
* Write a function that raises a name exception with a message.
