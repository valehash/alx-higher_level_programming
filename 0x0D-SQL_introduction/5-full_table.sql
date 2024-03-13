-- displays the description of the table first table from the database hbtn_0c_0
SELECT column_name, data_type, character_maximum_length, is_nullable, column_default
FROM information_schema.columns
where table_name = 'first_table';
