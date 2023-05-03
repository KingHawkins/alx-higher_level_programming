// Fetches and lists the 'title' for all movies
// using the starwars API

$(() => {
  $.get('https://swapi-api.hbtn.io/api/films/?format=json', (data, textStatus) => {
    if (textStatus === 'success') {
      const films = data.results;
      films.forEach(film => {
        $('#list_movies').append('<li>' + film.title + '</li>');
      });
    }
  });
});
