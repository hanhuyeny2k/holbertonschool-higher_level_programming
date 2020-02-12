#!/usr/bin/node
const request = require('request');
const url = 'http://swapi.co/api/films/' + process.argv[2];

request(url, { json: true }, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  console.log(body.title);
});
