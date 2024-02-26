#!/usr/bin/node
const fs = require('fs');

function writeToFile (filePath, content) {
  fs.writeFile(filePath, content, 'utf-8', (err) => {
    if (err) {
      console.log(err);
    }
  });
}

const filePath = process.argv[2];
const content = process.argv[3];
writeToFile(filePath, content);
