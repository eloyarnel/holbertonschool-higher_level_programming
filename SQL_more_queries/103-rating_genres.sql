-- Command that script that list all genres in the database htbn_0tvshows, and the average rating of all shows linked to each genre. The tables are linked as follows: tv_shows is linked to tv_show_genres by the show_id field, and tv_show_genres is linked to tv_genres by the genre_id field. The ratings of a show are in the tv_show_ratings table, which is linked to the tv_shows table by the show_id field. The results should be sorted in descending order by average rating, and ascending order by genre name for ties in average rating.
SELECT tv_genres.name, SUM(tv_show_ratings.rate) AS rating
FROM tv_genres
JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows
ON tv_show_genres.show_id = tv_shows.id
JOIN tv_show_ratings
ON tv_shows.id = tv_show_ratings.show_id
GROUP BY tv_genres.name
ORDER BY rating DESC;
