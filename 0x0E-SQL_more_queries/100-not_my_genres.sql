-- count
SELECT tv_genres.name FROM tv_genres WHERE tv_genres.id NOT IN (SELECT tv_show_genres.genre_id FROM tv_show_genres  WHERE tv_show_genres.show_id = (SELECT tv_shows.id FROM tv_shows WHERE tv_shows.title = 'Dexter') ) ORDER BY tv_genres.name ASC;

