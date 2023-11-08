#!/usr/bin/python3
"""This is FileStorage Module
"""
import json


class FileStorage:
    """This is FileStorage Class
        used to serialize and deserialize objects onto and from files
    """
    __file_path = 'file.json'
    __object = dict()

    def __init__(self):
        pass

    def all(self):
        """returns the dictionary __objects
        """
        pass

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id
        Attributes:
            obj (Python Object): The object to set
        """
        pass

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)
        """
        pass

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file 
        (__file_path) exists ; otherwise, do nothing. If the file doesnt
        exist, no exception should be raised)
        """
        pass