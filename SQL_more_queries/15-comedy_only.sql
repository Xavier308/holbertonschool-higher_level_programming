-- Only Comedy
-- Script that lists all Comedy shows in the database hbtn_0d_tvshows.

SELECT genres.name AS genre, COUNT(tv_show_genres.tv_show_id) AS number_of_shows
FROM genres
JOIN tv_show_genres ON genres.id = tv_show_genres.genre_id
GROUP BY genres.id
HAVING COUNT(tv_show_genres.tv_show_id) > 0
ORDER BY COUNT(tv_show_genres.tv_show_id) DESC;
