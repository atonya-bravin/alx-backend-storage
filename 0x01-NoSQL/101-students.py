#!/usr/bin/env python3
"""
This is a python script that contains a function that returns
all students sorted by average score
"""


def top_students(mongo_collection):
    """
    Function that returns all students sorted by average score
    """

    return list(mongo_collection.find())
