#!/usr/bin/node
const myInt = Number.parseInt(process.argv[2]);
if (Number.isNaN(myInt)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${myInt}`);
}
