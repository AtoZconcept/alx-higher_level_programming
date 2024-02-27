#!/usr/bin/node
const request = require('request');
const fs = require('fs');

const url = process.argv[2];
function writeToFile (filePath, content) {
  fs.writeFile(filePath, content, 'utf-8', (err) => {
    if (err) {
      console.log(err);
    }
  });
}
request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const filePath = process.argv[3];
    writeToFile(filePath, body);
  }
});
