#!/usr/bin/node
/**
 * Prints all characters of a Star Wars movie, in the same order
 * of the list "characters" in the /films/ response.
 * @param {string} movieId - The ID of the movie
 * @param {function} request - A function for making HTTP requests
 */
const { argv } = require('process');
const request = require('request');

const movieId = argv[2];
// The Star Wars API + The first positional arg passed as the Movie ID
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, movieData, body) => {
  if (error) {
    console.log(error);
  } else {
    movieData = JSON.parse(body);
    const characters = movieData.characters;
    /**
     * Gets the name of a Star Wars movie character
     * @param {number} idx - The index of the character in the list
     */
    function getCharacterName (idx) {
      if (idx < characters.length) {
        request(characters[idx], (error, characterData, body) => {
          if (error) {
            console.log(error);
          } else {
            characterData = JSON.parse(body);
            console.log(characterData.name);
            getCharacterName(idx + 1);
          }
        });
      }
    }
    getCharacterName(0);
  }
});
