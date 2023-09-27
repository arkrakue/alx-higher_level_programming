#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const apiUrl = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error('An error occurred:', error);
    return;
  }
  const film = JSON.parse(body);
  const characters = film.characters;
  const count = characters.length;
  characters.forEach(function(characterUrl, index) {
    request(characterUrl, function (error, response, body) {
      if (error) {
        console.error('An error occurred:', error);
        return;
      }
      const character = JSON.parse(body);
      console.log(character.name);
      if (index === count - 1) {
        console.log('All characters printed.');
      }
    });
  });
});

