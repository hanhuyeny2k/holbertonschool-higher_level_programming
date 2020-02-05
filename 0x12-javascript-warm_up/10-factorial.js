#!/usr/bin/node
function factorial (x) {
  if (isNaN(x) || x < 2) {
    return 1;
  }
  return x * factorial(x - 1);
}
const myVar = Number.parseInt(process.argv[2]);
console.log(factorial(myVar));
