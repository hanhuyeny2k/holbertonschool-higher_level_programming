#!/usr/bin/node
const myVar = Number.parseInt(process.argv[2]);
const i = 0, j = 0;
if (isNaN(myVar)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < myVar; i++) {
    for (let j = 0; j < myVar; j++) {
	  console.log('#');
    }
  }
}
