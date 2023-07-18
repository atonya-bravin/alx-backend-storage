# 0x01. NoSQL

## Objectives
This project is aimed at providing the knowledge in;
1. What NoSQL means
2. What is difference between SQL and NoSQL
3. What is ACID
4. What is a document storage
5. What are NoSQL types
6. What are benefits of a NoSQL database
7. How to query information from a NoSQL database
8. How to insert/update/delete information from a NoSQL database
9. How to use MongoDB

## Requirements
1. All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7) and PyMongo (version 3.10)
2. All your files should end with a new line
3. The first line of all your files should be exactly #!/usr/bin/env python3
4. A README.md file, at the root of the folder of the project, is mandatory
5. Your code should use the pycodestyle style (version 2.5.*)
6. The length of your files will be tested using wc
7. All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
8. All your functions should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)'
9. Your code should not be executed when imported (by using if __name__ == "__main__":)

## Tasks
The following are the some of the tasks set in order to test the knowledge gained.

### Task 0
Write a script that lists all databases in MongoDB.

#### Task 0 [Solution]
**Featured file** -> 0x01-NoSQL

### Task 1
Write a script that creates or uses the database my_db

#### Task 1 [Solution]
**Featured file** -> 1-use_or_create_database

### Task 2
Write a script that inserts a document in the collection school:

- The document must have one attribute name with value “Holberton school”
- The database name will be passed as option of mongo command

#### Task 2 [Solution]
**Featured file** -> 2-insert

### Task 3
Write a script that lists all documents in the collection school:

- The database name will be passed as option of mongo command

#### Taks 3 [Solution]
**Featured file** -> 3-all

