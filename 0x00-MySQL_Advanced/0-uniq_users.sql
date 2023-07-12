--This is a script file that creates a users table
Create TABLE IF NOT EXISTS users(
	id INT NOT NULL AUTO_INCREMENT,
	email varchar(255) NOT NULL UNIQUE,
	name varchar(255)
	);

