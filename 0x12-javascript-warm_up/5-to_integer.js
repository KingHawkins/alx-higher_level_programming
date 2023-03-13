#!/usr/bin/node
// prints argument is is integer convertible
if (process.argv.length < 3) {
  console.log('Not a number');
} else {
  if (Math.ceil(Number(process.argv[2]))) {
    console.log('My number: ' + Math.trunc(Number(process.argv[2])));
  } else {
    console.log('Not a number');
  }
}
