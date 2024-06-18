--  Genre ID for all shows
-- script that lists all shows contained in the database hbtn_0d_tvshows

-- List all shows along with their genre IDs, displaying NULL for shows without genres
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
