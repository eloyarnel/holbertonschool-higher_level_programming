-- Command to script all shows contained in the database that do not have a genre
SELECT shows.title, tv_shows_genres_genre.id
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.tv_show_id
WHERE tv_show_genres.genre_id IS NULL;
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
