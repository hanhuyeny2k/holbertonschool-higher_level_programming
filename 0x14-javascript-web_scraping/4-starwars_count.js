#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, { json: true }, (error, response, body) => {
  let counter = 0;
  if (error) throw error;
  for (const films of body.results) {
    for (const character of films.characters) {
      if (character.includes('18')) {
        counter++;
      }
    }
  }
  console.log(counter);
});
