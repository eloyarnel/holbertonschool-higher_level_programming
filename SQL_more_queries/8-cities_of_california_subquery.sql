-- COmmand to script that creates the database and the cities table
CREATE DATABASE IF NOT EXISTS hbtn_0e_4_usa;
USE hbtn_0e_4_usa;
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT UNIQUE NOT NULL,
    state_id INT NOT NULL,
    name VARCHAR(128) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
);
