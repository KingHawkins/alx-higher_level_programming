#!/usr/bin/node
// prints factorial
function factorial (a) {
  if (a === 1 || a === 0 || !Number(a)) {
    return (1);
  } else {
    return a * factorial(a - 1);
  }
}

console.log(factorial(parseInt(process.argv[2])));
