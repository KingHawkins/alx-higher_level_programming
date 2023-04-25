#!/usr/bin/node
// prints all characters of starwars movie
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    JSON.parse(body).characters.forEach((item) => {
      request(item, (error, response, body) => {
        if (!error && response.statusCode === 200) {
          console.log(JSON.parse(body).name);
        } else throw error;
      });
    });
  } else throw error;
});
