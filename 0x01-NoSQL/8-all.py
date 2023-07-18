#!/usr/bin/env python3
"""
This is a python script that lists all the documents in a collection
"""


def list_all(mongo_collection):
    """
    This is a function that lists all the documents in a collection
    """

    documents = mongo_collection.find()
    if documents.length == 0:
        return ([])

    else:
        for document in document:
            print(document)
