#!/usr/bin/node
const myVar = Number.parseInt(process.argv[2]);
if (isNaN(myVar)) {
  console.log('Missing size');
} else {
  let row = '';
  for (let i = 0; i < myVar; i++) {
    row += '#';
  }
  for (let i = 0; i < myVar; i++) {
    console.log(row);
  }
}
