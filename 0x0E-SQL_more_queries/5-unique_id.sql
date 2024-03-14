-- sql code to create a table a field that can't be empty
CREATE TABLE IF NOT EXISTS unique_id(
  id INT NOT NULL DEFAULT 1 UNIQUE,
  name VARCHAR(256)
);
