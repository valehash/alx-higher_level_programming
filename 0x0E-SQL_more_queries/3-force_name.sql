-- sql code to create a table a field that can't be empty
CREATE TABLE IF NOT EXISTS forcename(
  id INT,
  name VARCHAR(256) NOT NULL
);

