#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const array = [];
    while (this.width > 0) {
      array.push('X');
      this.width--;
    }
    while (this.height > 0) {
      console.log(array.join(',').replaceAll(',', ''));
      this.height--;
    }
  }
}
module.exports = Rectangle;
