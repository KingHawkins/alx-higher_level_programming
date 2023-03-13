#!/usr/bin/node
// executes x times
exports.callMeMoby = function (x, theFunction) {
  let item = 0;
  while (item < x) {
    theFunction();
    item++;
  }
};
