#!/usr/bin/env python3
"""
This is a python script that lists all the documents in a collection
"""


def list_all(mongo_collection):
    """
    This is a function that lists all the documents in a collection
    """

    return [each for each in mongo_collection.find()]
