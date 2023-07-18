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

### Task 9
Write a Python function that inserts a new document in a collection based on kwargs:

- Prototype: def insert_school(mongo_collection, **kwargs):
- mongo_collection will be the pymongo collection object
- Returns the new _id
  
  
**9-main.py**
```
#!/usr/bin/env python3
""" 9-main """
from pymongo import MongoClient
list_all = __import__('8-all').list_all
insert_school = __import__('9-insert_school').insert_school

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    school_collection = client.my_db.school
    new_school_id = insert_school(school_collection, name="UCSF", address="505 Parnassus Ave")
    print("New school created: {}".format(new_school_id))

    schools = list_all(school_collection)
    for school in schools:
        print("[{}] {} {}".format(school.get('_id'), school.get('name'), school.get('address', "")))
```

#### Task 9 [Solution]
**Featured file** -> 9-insert_school.py

#### Task 9 [Solution Breakdown]
We use the insert_one() method to insert a predefined dictionary as a document into a collection
```
return mongo_collection.insert_one(kwargs).inserted_id
```

### Task 10
Write a Python function that changes all topics of a school document based on the name:

- Prototype: def update_topics(mongo_collection, name, topics):
- mongo_collection will be the pymongo collection object
- name (string) will be the school name to update
- topics (list of strings) will be the list of topics approached in the school
  
  
**10-main.py**
```
#!/usr/bin/env python3
""" 10-main """
from pymongo import MongoClient
list_all = __import__('8-all').list_all
update_topics = __import__('10-update_topics').update_topics

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    school_collection = client.my_db.school
    update_topics(school_collection, "Holberton school", ["Sys admin", "AI", "Algorithm"])

    schools = list_all(school_collection)
    for school in schools:
        print("[{}] {} {}".format(school.get('_id'), school.get('name'), school.get('topics', "")))

    update_topics(school_collection, "Holberton school", ["iOS"])

    schools = list_all(school_collection)
    for school in schools:
        print("[{}] {} {}".format(school.get('_id'), school.get('name'), school.get('topics', "")))
```

#### Task 10 [Solution]
**Featured file** -> 10-update_topics.py

#### Task 10 [Solution Breakdown]
In this task, we are using the update_many() method to update many instances with a specific criteria.
```
mongo_collection.update_many(
        { 'name': name },
        { '$set': { 'topics': topics }}
    )
```

### Task 11
Write a Python function that returns the list of school having a specific topic:

- Prototype: def schools_by_topic(mongo_collection, topic):
- mongo_collection will be the pymongo collection object
- topic (string) will be topic searched
  
  
**11-main.py**
```
#!/usr/bin/env python3
""" 11-main """
from pymongo import MongoClient
list_all = __import__('8-all').list_all
insert_school = __import__('9-insert_school').insert_school
schools_by_topic = __import__('11-schools_by_topic').schools_by_topic

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    school_collection = client.my_db.school

    j_schools = [
        { 'name': "Holberton school", 'topics': ["Algo", "C", "Python", "React"]},
        { 'name': "UCSF", 'topics': ["Algo", "MongoDB"]},
        { 'name': "UCLA", 'topics': ["C", "Python"]},
        { 'name': "UCSD", 'topics': ["Cassandra"]},
        { 'name': "Stanford", 'topics': ["C", "React", "Javascript"]}
    ]
    for j_school in j_schools:
        insert_school(school_collection, **j_school)

    schools = schools_by_topic(school_collection, "Python")
    for school in schools:
        print("[{}] {} {}".format(school.get('_id'), school.get('name'), school.get('topics', "")))
```

#### Task 11 [Solution]
**Featured file** -> 11-schools_by_topic.py

#### Task 11 [Solution Breakdown]
Used the find() method to filter out the schoold using the topic in them
```
return mongo_collection.find({'topics': topic})
```

