# Javascript - Web Scraping
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
## Install 'request' module and use it
```
$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules
```
## Execution
`$ chmod u+x <filename>`
`$ ./<filename>`

## Example
```
$ ./0-readme.js cisfun
C is super fun!
$ cat cisfun
C is super fun!
$ ./0-readme.js doesntexist
{ Error: ENOENT: no such file or directory, open 'doesntexist'
    at Error (native)
  errno: -2,
  code: 'ENOENT',
  syscall: 'open',
  path: 'doesntexist' }
$ 
```
## Tasks
0) Write a script that reads and prints the content of a file.
1) Write a script that writes a string to a file.
2) Write a script that display the status code of a GET request.
3) Write a script that prints the title of a Star Wars movie where the episode number matches a given integer.
4) Write a script that prints the number of movies where the character Wedge Antilles is present.
5) Write a script that gets the contents of a webpage and stores it in a file.
6) Write a script that computes the number of tasks completed by user id.
