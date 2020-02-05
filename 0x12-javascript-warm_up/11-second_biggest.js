#!/usr/bin/node
const myVar = process.argv[2];
const max = Math.max.apply(null, myVar);
myVar.splice(myVar.indexOf(max), 1);
console.log(max);
