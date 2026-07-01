-- Command that list all shows without the genre Comedy in the hbtn_0tvshows database. The tables are linked as follows: tv_shows is linked to tv_show_genres by the show_id field, and tv_show_genres is linked to tv_genres by the genre_id field. The results should be sorted in ascending order by show title.
SELECT title
FROM tv_shows
WHERE id NOT IN (
    SELECT tv_shows.id
    FROM tv_shows
    JOIN tv_show_genres
    ON tv_shows.id = tv_show_genres.show_id
    JOIN tv_genres
    ON tv_show_genres.genre_id = tv_genres.id
    WHERE tv_genres.name = 'Comedy'
)
ORDER BY title;
