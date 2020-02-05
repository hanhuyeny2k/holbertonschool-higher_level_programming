#!/usr/bin/node
function add (a, b) {
  return arg1 + arg2;
}

const arg1 = Number.parseInt(process.argv[2]);
const arg2 = Number.parseInt(process.argv[3]);
console.log(add(arg1, arg2));
