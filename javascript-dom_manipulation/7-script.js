// Script that fetches and lists the title for all movies by using a URL
document.addEventListener('DOMContentLoaded', function() {
    const apiUrl = 'https://swapi-api.hbtn.io/api/films/?format=json';

    fetch(apiUrl)
      .then(response => response.json())
      .then(data => {
        const listMoviesUl = document.getElementById('list_movies');
        data.results.forEach(movie => {
          const listItem = document.createElement('li');
          listItem.textContent = movie.title;
          listMoviesUl.appendChild(listItem);
        });
      })
      .catch(error => console.error('Error fetching data:', error));
  });
