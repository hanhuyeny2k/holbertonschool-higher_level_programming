# Python - Network #0

## Requirements
* Allowed editors: vi, vim, emacs
* A README.md file, at the root of the folder of the project, is mandatory
* All the scripts will be tested on Ubuntu 14.04 LTS
* All the Bash scripts should be exactly 3 lines long (wc -l file should print 3)
* All the files should end with a new line
* All the files must be executable
* The first line of all the bash files should be exactly #!/bin/bash
* The second line of all the Bash scripts should be a comment explaining what is the script doing
* All curl commands must be have the option -s (silent mode)
* All the files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
* The first line of all the Python files should be exactly #!/usr/bin/python3
* The code should use the PEP 8 style (version 1.7.*)
* All the modules should be documented: python3 -c 'print(__import__("my_module").__doc__)'
* All the classes should be documented: python3 -c 'print(__import__("my_module").MyClass.__doc__)'
* All the functions (inside and outside a class) should be documented: python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'

## Execution
`chmod u+x <filename>`

`python3 <filename>`

## Example
```
$ ./0-body_size.sh 0.0.0.0:5000
10
$
```
```
$ cat 6-main.py
#!/usr/bin/python3
""" Test function find_peak """
find_peak = __import__('6-peak').find_peak

print(find_peak([1, 2, 4, 6, 3]))
print(find_peak([4, 2, 1, 2, 3, 1]))
print(find_peak([2, 2, 2]))
print(find_peak([]))
print(find_peak([-2, -4, 2, 1]))
print(find_peak([4, 2, 1, 2, 3, 1]))

$ ./6-main.py
6
3
2
None
2
4
$ wc -l 6-peak.txt 
2 6-peak.txt
```
# Tasks
0) Write a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
	* The size must be displayed in bytes
	* You have to use curl
Please test your script in the container provided, using the web server running on port 5000
1) Write a Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response
	* Display only body of a 200 status code response
	* You have to use curl
Please test your script in the container provided, using the web server running on port 5000
2) Write a Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response
	* You have to use curl
Please test your script in the container provided, using the web server running on port 5000
3) Write a Bash script that takes in a URL and displays all HTTP methods the server will accept.
	* You have to use curl
Please test your script in the container provided, using the web server running on port 5000
4) Write a Bash script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response
	* A header variable X-HolbertonSchool-User-Id must be sent with the value 98
	* You have to use curl
Please test your script in the container provided, using the web server running on port 5000
5) Write a Bash script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response
	* A variable email must be sent with the value hr@holbertonschool.com
	* A variable subject must be sent with the value I will always be here for PLD
	* You have to use curl
Please test your script in the container provided, using the web server running on port 5000
6) Write a function that finds a peak in a list of unsorted integers.
	* Prototype: def find_peak(list_of_integers):
	* You are not allowed to import any module
	* Your algorithm must have the lowest complexity
	* 6-peak.py must contain the function
	* 6-peak.txt must contain the complexity of your algorithm: O(log(n)), O(n), O(nlog(n)) or O(n2) 
