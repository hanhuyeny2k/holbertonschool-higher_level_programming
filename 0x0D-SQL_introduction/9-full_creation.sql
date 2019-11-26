-- Create the table second_table in the database and add multiple rows
CREATE TABLE IF NOT EXISTS second_table (
	id INT,
	name VARCHAR(256),
	score INT
);
INSERT INTO second_table (id, name, score) VALUES
(1,'JOHN', 10),
(2,'JOHN', 10),
(3,'JOHN', 10),
(4,'JOHN', 10);
