#!/usr/bin/node
const myVar = process.argv.slice(2);
if (typeof myVar[0] === 'undefined') {
  console.log('No argument');
} else {
  console.log(myVar[0]);
}
