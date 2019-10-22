# Python - Almost A Circle

## Prerequesites
### Python Scripts
* Allowed editors: vi, vim, emacs
* All the files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
* All the files should end with a new line
* The first line of the your files should be exactly #!/usr/bin/python3
* A README.md file, at the root of the folder of the project, is mandatory
* The code should use the PEP 8 style (version 1.7.*)
* All the files must be executable
* The length of the files will be tested using wc
* All the modules should be documented: python3 -c 'print(__import__("my_module").__doc__)'
* All the classes should be documented: python3 -c 'print(__import__("my_module").MyClass.__doc__)'
* All the functions (inside and outside a class) should be documented: python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'

### Python Unit Tests
* Allowed editors: vi, vim, emacs
* All the files should end with a new line
* All the test files should be inside a folder tests
* Have to use the unittest module
* All the test files should be python files (extension: .py)
* All the test files and folders should start with test_
* The file organization in the tests folder should be the same as your project: ex: for models/base.py, unit tests must be in: tests/test_models/test_base.py
* All the tests should be executed by using this command: python3 -m unittest discover tests
* Also test file by file by using this command: python3 -m unittest tests/test_models/test_base.py

## Compilation
`$ chmod u+x *.py`

`$ ./1-main.py`

## Example
```$ cat 0-main.py
#!/usr/bin/python3
""" 0-main """
from models.base import Base

if __name__ == "__main__":

    b1 = Base()
    print(b1.id)

    b2 = Base()
    print(b2.id)

    b3 = Base()
    print(b3.id)

    b4 = Base(12)
    print(b4.id)

    b5 = Base()
    print(b5.id)

$ ./0-main.py
1
2
3
12
4
```

## Tasks
* Write test cases for all the files and be validated with PEP8.
* Write the first class Base.
* Write the class Rectangle that inherits from Base.
* Update the class Rectangle by adding validation of all setter methods and instantiation (id excluded).
* Update the class Rectangle by adding the public method def area(self): that returns the area value of the Rectangle instance.
* Update the class Rectangle by adding the public method def display(self): that prints in stdout the Rectangle instance with the character # - you dont need to handle x and y here.
* Update the class Rectangle by overriding the __str__ method so that it returns [Rectangle] (<id>) <x>/<y> - <width>/<height>.
* Update the class Rectangle by improving the public method def display(self): to print in stdout the Rectangle instance with the character # by taking care of x and y.
* Update the class Rectangle by adding the public method def update(self, *args): that assigns an argument to each attribute.
* Update the class Rectangle by updating the public method def update(self, *args): by changing the prototype to update(self, *args, **kwargs) that assigns a key/value argument to attributes.
* Write the class Square that inherits from Rectangle.
* Update the class Square by adding the public getter and setter size.
* Update the class Square by adding the public method def update(self, *args, **kwargs) that assigns attributes.
* Update the class Rectangle by adding the public method def to_dictionary(self): that returns the dictionary representation of a Rectangle.
* Update the class Square by adding the public method def to_dictionary(self): that returns the dictionary representation of a Square.
* Update the class Base by adding the static method def to_json_string(list_dictionaries): that returns the JSON string representation of list_dictionaries.
* Update the class Base by adding the class method def save_to_file(cls, list_objs): that writes the JSON string representation of list_objs to a file.
* Update the class Base by adding the static method def from_json_string(json_string): that returns the list of the JSON string representation json_string.
* Update the class Base by adding the class method def create(cls, **dictionary): that returns an instance with all attributes already set.
* Update the class Base by adding the class method def load_from_file(cls): that returns a list of instances. 
