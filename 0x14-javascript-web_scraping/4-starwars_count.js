#!/usr/bin/node
// Prints the number of movies where the character "Wedge Antilles" is.
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/people/18/';
request(process.argv[2], (error, response, body) => {
  if (!error && response.statusCode === 200) {
    let count = 0;
    for (const item of JSON.parse(body).results) {
      if (item.characters.includes(url)) {
        count += 1;
      }
    }
    console.log(count);
  } else throw error;
});
