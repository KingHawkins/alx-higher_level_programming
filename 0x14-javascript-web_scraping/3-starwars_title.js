#!/usr/bin/node
// prints title of a Star war's movie fetched from the Starwars API
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    console.log(JSON.parse(body).title);
  } else {
    throw error;
  }
});
