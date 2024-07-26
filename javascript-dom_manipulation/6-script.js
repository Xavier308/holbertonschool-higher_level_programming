// Script that fetches the character name from a URL
document.addEventListener('DOMContentLoaded', function() {
    const apiUrl = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

    fetch(apiUrl) // Makes a request to the API
      .then(response => response.json()) // Parses the response as JSON
      .then(data => {
        const characterDiv = document.getElementById('character');
        characterDiv.textContent = data.name;
      })
      .catch(error => console.error('Error fetching data:', error)); // Logs any errors to the console
  });
  