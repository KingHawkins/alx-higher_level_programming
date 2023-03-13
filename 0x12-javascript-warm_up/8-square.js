#!/usr/bin/node
// pprints a square
if (!Number(process.argv[2]) || process.argv.length < 3) {
  console.log('Missing size');
} else {
  let parsed = parseInt(process.argv[2]);
  const array = [];
  while (parsed > 0) {
    array.push('X');
    parsed--;
  }
  array.forEach(() => {
    console.log(array.join(',').replaceAll(',', ''));
  }
  );
}
