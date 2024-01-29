#!/usr/bin/node

const axios = require('axios');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

axios.get(apiUrl)
  .then(response => {
    const filmData = response.data;
    const characters = filmData.characters;

    if (characters.length === 0) {
      console.log(`No characters found for Movie ID ${movieId}`);
    } else {
      characters.forEach(characterUrl => {
        axios.get(characterUrl)
          .then(charResponse => {
            const characterData = charResponse.data;
            console.log(characterData.name);
          })
          .catch(charError => {
            console.error('Error fetching character data:', charError.message);
          });
      });
    }
  })
  .catch(error => {
    console.error('Error fetching film data:', error.message);
    process.exit(1);
  });
