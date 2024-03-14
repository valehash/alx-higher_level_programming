-- create a database if not exist
CREATE DATABASE IF NOT EXISTS  hbtn_0d_usa;
-- sql code to create a table if it doesn't exist
CREATE TABLE IF NOT EXISTS states (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(256) NOT NULL
);
