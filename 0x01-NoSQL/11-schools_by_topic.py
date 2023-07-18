#!/usr/bin/env python3
"""
This is a script that contains a method that
returns the list of school having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    This method returns the list of school having a specific topic
    """

    return mongo_collection.find({"topics": topic})
