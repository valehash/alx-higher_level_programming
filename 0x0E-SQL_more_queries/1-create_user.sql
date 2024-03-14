-- sql code to create a user with a passowrd
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- grants the user all priviledges
GRANT ALL PRIVILEGES ON *.* to 'user_0d_1'@'localhost'; 
