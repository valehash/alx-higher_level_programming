#!/usr/bin/node
// code to get the title of starwars using the api

const name = 'https://swapi-api.alx-tools.com/api/films/';

const id = process.argv[2];

const url = name + id;

const req = require('request');

console.log(url);

req(url, { json: true }, (error, response, body) => {
  if (error) console.error(error);

  console.log(body.title);

  console.log(body.title);
});
