#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];
const characterId = '18'; // Wedge Antilles

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error('An error occurred:', error);
    return;
  }
  const films = JSON.parse(body).results;
  const count = 0;
  films.forEach(function(film) {
    if (film.characters.includes(characterId)) {
      count++;
    }
  });
  console.log(count);
});

