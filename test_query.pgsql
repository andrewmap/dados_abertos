CREATE TEMPORARY TABLE temp_table (
  id SERIAL PRIMARY KEY,
  name_id VARCHAR(50)
);

INSERT INTO temp_table (name_id)
VALUES ('A'), ('B');

select * from temp_table