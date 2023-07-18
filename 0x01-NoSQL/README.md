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

### Task 4
Write a script that lists all documents with name="Holberton school" in the collection school:

- The database name will be passed as option of mongo command

#### Taks 4 [Solution]
**Featured file** -> 4-match

### Task 5
Write a script that displays the number of documents in the collection school:

- The database name will be passed as option of mongo command

#### Task 5 [Solution]
**Featured file** -> 5-count

### Task 6
Write a script that adds a new attribute to a document in the collection school:

- The script should update only document with name="Holberton school" (all of them)
- The update should add the attribute address with the value “972 Mission street”
- The database name will be passed as option of mongo command

#### Task 6 [Solution]
**Featured file** -> 6-update

### Task 7
Write a script that deletes all documents with name="Holberton school" in the collection school:

- The database name will be passed as option of mongo command

#### Task 7 [Solution]
**Featured file** -> 7-delete

### Task 8
Write a Python function that lists all documents in a collection:

- Prototype: def list_all(mongo_collection):
- Return an empty list if no document in the collection
- mongo_collection will be the pymongo collection object
  
  
**8-main.py**  
```
#!/usr/bin/env python3
""" 8-main """
from pymongo import MongoClient
list_all = __import__('8-all').list_all

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    school_collection = client.my_db.school
    schools = list_all(school_collection)
    for school in schools:
        print("[{}] {}".format(school.get('_id'), school.get('name')))
```

#### Task 8 [Solution]
**Featured file** -> 8-all.py

#### Task 8 [Solution Beakdown]
In this task, we use list comprehension to deliver the right list of available documents in a collection
```
return [each for each in mongo_collection.find()]
```
- With the syntax **new_list = [expression for item in iterable if condition]**
- We use the find() method of the mongo_collection object to retrieve all the documents in the collection.
- Since find() returns a cursor object that can be iterated over to retrieve each document, we use a list comprehension to create a list of all the documents returned by the cursor.
