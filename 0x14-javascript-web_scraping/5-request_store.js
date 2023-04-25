#!/usr/bin/node
// Gets the contents of a webpage and stores in a file
const request = require('request');
const fs = require('fs');
request(process.argv[2], (error, response, body) => {
  if (!error && response.statusCode === 200) {
    fs.writeFile(process.argv[3], body, 'utf8', (err) => {
      if (err) {
        throw err;
      }
    });
  } else console.error('Bad Request', error);
});
