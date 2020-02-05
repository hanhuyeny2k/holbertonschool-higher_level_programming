#!/usr/bin/node
const myVar = process.argv.slice(2);
const str1 = myVar[0];
const str2 = myVar[1];
if (typeof myVar[0] === 'undefined') {
  console.log('undefined is undefined');
} else {
  console.log(str1.concat(' is ', str2));
}
