-- Command a script that lists all cities of California that can be found in the database hbtn_0e_4_usa
SELECT cities.name
FROM cities
WHERE cities.state_id = (SELECT states.id FROM states WHERE states.name = 'California');
