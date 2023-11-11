#!/usr/bin/python3
"""module for FileStorage class"""
import json
import datetime
import os

class FileStorage:
    """class for data storage and retrieval"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__,obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as fp:
            dic = {ky: vl.to_dict() for ky, vl in FileStorage.__objects.items()}
            json.dump(dic, fp)

    def reload(self):
        """reloads the objects stored"""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as fp:
            obj_dict = json.load(fp)
            obj_dict = {ky: self.classes()[vl["__class__"]](**vl)
                    for ky, vl in obj_dict.items()}
            FileStorage.__objects = obj_dict

