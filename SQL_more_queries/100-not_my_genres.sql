-- Command that script that uses the hbtn_0tvshows database to list all genres that are not linked to the show Dexter. The tables are linked as follows: tv_shows is linked to tv_show_genres by the show_id field, and tv_show_genres is linked to tv_genres by the genre_id field. The results should be sorted in ascending order by genre name.
SELECT name
FROM tv_genres
WHERE id NOT IN (
    SELECT genre_id
    FROM tv_show_genres
    JOIN tv_shows
    ON tv_show_genres.show_id = tv_shows.id
    WHERE tv_shows.title = 'Dexter'
)
ORDER BY name;
