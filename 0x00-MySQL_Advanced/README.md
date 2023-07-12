# 0x00. MySQL advanced
This is a project that builds on the MySQL advanced skills.

## Objective
This project is aimed at providing knowledge about;
1. How to create tables with constraints
2. How to optimize queries by adding indexes
3. What is and how to implement stored procedures and functions in MySQL
4. What is and how to implement views in MySQL
5. What is and how to implement triggers in MySQL

## General Requirements
1. All the files will be executed on Ubuntu 18.04 LTS using MySQL 5.7 (version 5.7.30)
2. All the files should end with a new line
3. All the SQL queries should have a comment just before (i.e. syntax above)
4. All the files should start by a comment describing the task
5. All SQL keywords should be in uppercase (SELECT, WHERE…)
6. A README.md file, at the root of the folder of the project, is mandatory
7. The length of your files will be tested using wc

## Building blocks
**comments by example**  
```
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
```  
    
**How to import a SQL dump**
```
$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
Enter password: 
$ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
$ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
Enter password:
``` 

## Featured Tasks
### Task 0
Write a SQL script that creates a table users following these requirements:  
  
- With these attributes:
	- id, integer, never null, auto increment and primary key
	- email, string (255 characters), never null and unique
	- name, string (255 characters)
- If the table already exists, your script should not fail
- Your script can be executed on any database
**Context: Make an attribute unique directly in the table schema will enforced your business rules and avoid bugs in your application**  
  
#### Task 0 [Solution]
**Featured file** -> 0-uniq_users.sql

#### Task 0 [Solution Breakdown]
- Check for the existance of the table and delete it if present.
```
DROP TABLE IF EXISTS users;
```
- Creation of the table, defining the constrants given

### Task 1
Write a SQL script that creates a table users following these requirements:

- With these attributes:
	- id, integer, never null, auto increment and primary key
	- email, string (255 characters), never null and unique
	- name, string (255 characters)
	- country, enumeration of countries: US, CO and TN, never null (= default will be the first element of the enumeration, here US)
- If the table already exists, your script should not fail
- Your script can be executed on any database

#### Task 1 [Solution]
**Featured file** -> 1-country_users.sql

#### Task 1 [Solution Breakdown]
- Check for the existance of the table and delete it if present.
```
DROP TABLE IF EXISTS users;
```
- Creation of the table, defining the constrants given
- The country attribute is defined as an ENUM type with three possible values: 'US', 'CO', and 'TN'. It is marked as NOT NULL, meaning a value must be provided for this attribute. Additionally, a default value of 'US' is set for the "country" attribute, which will be used if no explicit value is provided during an INSERT operation.

