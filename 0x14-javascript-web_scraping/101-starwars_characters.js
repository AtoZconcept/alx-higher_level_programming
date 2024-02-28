#!/usr/bin/node
const request = require('request');

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

const fetchCharacter = async (characterUrl) => {
  return new Promise((resolve, reject) => {
    request.get(characterUrl, (characterError, characterResponse, characterBody) => {
      if (characterError) {
        reject(characterError);
      } else {
        const characterName = JSON.parse(characterBody);
        resolve(characterName.name);
      }
    });
  });
};

request.get(url, async (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const films = JSON.parse(body);
    for (const characterUrl of films.characters) {
      try {
        const characterName = await fetchCharacter(characterUrl);
        console.log(characterName);
      } catch (characterError) {
        console.error(characterError);
      }
    }
  }
});
