#!/usr/bin/node
// prints second bigggest
function secondBiggest (arr) {
  const sorted = arr.sort((a, b) => {
    return a - b;
  }
  );
  return sorted.slice(sorted.length - 2, sorted.length - 1).join();
}
let array = '';
array += process.argv;
console.log(secondBiggest(array.split(',').splice(2)));
