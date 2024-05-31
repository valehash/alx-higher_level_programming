#!/usr/bin/node
// code to get the title of starwars using the api


const request = require('request');
const name = process.argv[2];

const url = 'https://swapi-api.alx-tools.com/api/films/';
const result = url.concat(name);

request(result, { json: true }, (error, response, body) => {
  if (error) console.log(error);

  console.log(body.title);
});
