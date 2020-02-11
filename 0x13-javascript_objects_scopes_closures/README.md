# Javascript - Objects, Scopes and Closures
## Requirements
* Allowed editors: vi, vim, emacs
* All the files will be interpreted on Ubuntu 14.04 LTS using node (version 10.14.x)
* All the files should end with a new line
* The first line of all the files should be exactly #!/usr/bin/node
* A README.md file, at the root of the folder of the project, is mandatory
* The code should be semistandard compliant. Rules of Standard + semicolons on top. Also as reference: AirBnB style
* All the files must be executable
* The length of the files will be tested using wc
* Not allowed to use var
## Install Node 10
```
$ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```
## Install semi-standard
`$ sudo npm install semistandard --global`

## Execution
`$ chmod u+x <filename>`
`$ ./<filename>`

## Example
```
$ cat 0-main.js
#!/usr/bin/node
const Rectangle = require('./0-rectangle');

const r1 = new Rectangle();
console.log(r1);
console.log(r1.constructor);

$ ./0-main.js
Rectangle {}
[Function: Rectangle]
$ 
```
## Tasks
* Write a class Rectangle that defines a rectangle including width and height.
	* Create an instance method called print(), rotate(), double().
* Write a class Square that defines a square and inherits from Rectangle.
* Write a function that returns the number of occurrences in a list.
* Write a function that returns the reversed version of a list.
* Write a function that prints the number of arguments already printed and the new argument value.
* Write a function that converts a number from base 10 to another base passed as argument.
