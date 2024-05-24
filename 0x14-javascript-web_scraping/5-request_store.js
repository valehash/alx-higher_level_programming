#!/usr/bin/node
// code to get the title of starwars using the api
const url = process.argv[2];

const fs = require('node:fs')

const req = require('request');

const filename = 'loremimpsom';
console.log(url);

req(url, (error, response, body) => {
  if (error) {
    console.error(error);
  }

  fs.writeFile(filename, body, err =>  {
    if (err) {
      console.error(err);
    }
  });
});
