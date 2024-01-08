#!/usr/bin/node
function factorial (num) {
  if (isNaN(num) || num < 1) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}

const arg = parseInt(process.argv[2]);
console.log(factorial(arg));
