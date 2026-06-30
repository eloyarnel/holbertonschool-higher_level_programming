-- Command that script that list all records of the table second_table of the current database.
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
