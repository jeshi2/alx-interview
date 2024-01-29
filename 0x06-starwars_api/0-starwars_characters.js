#!/usr/bin/node

const util = require('util');
const axios = require('axios');

const filmID = process.argv[2];

async function starwarsCharacters(filmId) {
  const endpoint = `https://swapi-api.hbtn.io/api/films/${filmId}`;
  try {
    const response = await axios.get(endpoint);
    const filmData = response.data;
    const characters = filmData.characters;

    for (const characterUrl of characters) {
      const characterResponse = await axios.get(characterUrl);
      const characterData = characterResponse.data;
      console.log(characterData.name);
    }
  } catch (error) {
    console.error('Error:', error.message);
    process.exit(1);
  }
}

starwarsCharacters(filmID);