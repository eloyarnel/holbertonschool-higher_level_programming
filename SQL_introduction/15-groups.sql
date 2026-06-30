-- Command that script that list the number of records with the same score in the table second_table of the current database.
SELECT score, COUNT(*) AS count
FROM second_table
GROUP BY score
ORDER BY number DESC;
