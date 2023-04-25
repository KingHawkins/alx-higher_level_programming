#!/usr/bin/node
// Reads and prints contents of a file
// Contents of the file must be read in utf-8
// if an error occurs, print the error object
const fs = require('fs');

fs.readFile(process.argv[2], 'utf8', function (err, contents) {
  if (contents === undefined) {
    console.log(err);
  } else {
    console.log(contents);
  }
});
