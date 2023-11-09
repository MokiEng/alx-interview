#!/usr/bin/node
const axios = require('axios');

const getMovieCharacters = async (movieId) => {
  try {
    // Fetch movie details
    const response = await axios.get(`https://swapi.dev/api/films/${movieId}/`);
    const characters = response.data.characters;

    // Fetch character details
    const characterDetails = await Promise.all(
      characters.map(async (characterUrl) => {
        const characterResponse = await axios.get(characterUrl);
        return characterResponse.data.name;
      })
    );

    return characterDetails;
  } catch (error) {
    console.error(`Error: ${error.message}`);
    return [];
  }
};

const printMovieCharacters = async (movieId) => {
  const characters = await getMovieCharacters(movieId);
  characters.forEach((character) => console.log(character));
};

// Get movie ID from command line arguments
const movieId = process.argv[2];

// Check if a movie ID is provided
if (!movieId) {
  console.error('Please provide a movie ID as a command line argument.');
} else {
  printMovieCharacters(movieId);
}
