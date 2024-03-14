-- create a database if not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- sql code to create a user with a passowrd
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- grants the user all priviledges
GRANT SELECT ON hbtn_0d_2.* to 'user_0d_2'@'localhost';
