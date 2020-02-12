#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, { json: true }, (error, response, body) => {
  const dict = {};
  if (error) throw error;
  for (const task of body) {
    if (task.completed) {
      if (dict[task.userId]) {
        dict[task.userId]++;
      } else {
        dict[task.userId] = 1;
      }
    }
  }
  console.log(dict);
});
