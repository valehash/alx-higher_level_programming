#!/usr/bin/node
// Write a script that computes the number of tasks completed by user id

const name = process.argv[2];
const request = require('request');

request(name, { json: true }, (err, response, body) => {
  if (err) console.error(err);

  const new_todos = {};
  for (const i of body) {
    if (i.completed === true) {
      if (new_todos[i.userId] === undefined) {
        new_todos[i.userId] = 0;
      }
      new_todos[i.userId] += 1;
    }
  }
  console.log(new_todos);
});
