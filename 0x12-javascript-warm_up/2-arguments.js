#!/usr/bin/node
const myVar = process.argv.slice(2);
if (myVar.length >= 2) {
  console.log('Argument found');
} else if (myVar.length === 1) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
