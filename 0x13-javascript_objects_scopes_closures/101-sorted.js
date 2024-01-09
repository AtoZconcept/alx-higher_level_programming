#!/usr/bin/node
const { dict } = require('./101-data');

const reverseDict = Object.entries(dict).reduce((acc, [key, value]) => {
  acc[value] = [...(acc[value] || []), key];
  return acc;
}, {});

console.log(reverseDict);
