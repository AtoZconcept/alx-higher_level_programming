#!/usr/bin/node
const fs = require('fs');

function readAndPrint(filePath) {
    fs.readFile(filePath, 'utf-8', (err, data) => {
        if (err) {
            console.log(err);
        } else {
            console.log(data);
        }
    });
}

if (process.argv.length < 3) {
    console.error('Usage: node scipty.js <file>');
    process.exit(1);
}

const filePath = process.argv[2];
readAndPrint(filePath);
