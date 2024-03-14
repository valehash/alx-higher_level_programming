-- sql code to create a table a field that can't be empty
CREATE TABLE IF NOT EXISTS  id_not_null(
  id INT NOT NULL DEFAULT 1,
  name VARCHAR(256)
);
