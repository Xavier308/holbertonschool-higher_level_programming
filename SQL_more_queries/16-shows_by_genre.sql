-- List shows and genres
-- script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.

-- List all shows and their linked genres, showing NULL for shows without a genre
SELECT tv_shows.title, genres.name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN genres ON genres.id = tv_show_genres.genre_id
ORDER BY tv_shows.title ASC, genres.name ASC;
