#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const films = JSON.parse(body).results;
    const wedgeAntillesFilms = films.filter(film => film.characters.some(character => character.include('18')));
    console.log(wedgeAntillesFilms.length);
  }
});
