#!/usr/bin/node
const request = require('request');

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;
request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const films = JSON.parse(body);
    films.characters.forEach(characterUrl => {
      request.get(characterUrl, (characterError, characterResponse, characterBody) => {
        if (characterError) {
          console.error(characterError);
        } else {
          const characterName = JSON.parse(characterBody);
          console.log(characterName.name);
        }
      });
    });
  }
});
