-- Command that lists all shows, and all genres linked to each show, sorted by show title and genre name (ascending). If a show has no genre, display NULL for the genre name. The tables are linked as follows: tv_shows is linked to tv_show_genres by the show_id field, and tv_show_genres is linked to tv_genres by the genre_id field.
SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title ASC, tv_genres.name ASC;
