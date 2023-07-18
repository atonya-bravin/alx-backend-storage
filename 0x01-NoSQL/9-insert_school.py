#!/usr/bin/env python3
"""
This is a python script that contains a script that
inserts a new document in a collection based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """
    This method inserts a new document in a collection based on kwargs
    """

    return mongo_collection.insertMany(kwargs).inserted_id
