#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

request(url, function (error, response, body) {
  if (error) {
    console.error('An error occurred:', error);
    return;
  }
  const movie = JSON.parse(body);
  console.log( movie.title);
});

