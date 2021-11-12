#!/usr/bin/python3
import json
import os


class FileStorage:
    """ Class FileStorage  """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Return all Objects """
        return FileStorage.__objects

    def new(self, obj):
        """ Create New Object """
        FileStorage.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj
        
    def save(self):
        """ Save File in JSON """
        with open(FileStorage.__file_path, 'w') as file_json:
            res = {}
            for key, value in FileStorage.__objects.items():
                res[key] = value.to_dict()
            file_json.write(json.dumps(res))

    def reload(self):
        """ Reload File Json """
        try:
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as file_json:
                from models.base_model import BaseModel

                json_des = json.load(file_json)

            for key, value in json_des.items():
                value = eval(value["__class_"])(**value)
                FileStorage.__objects[key] = value
        except OSError:
            pass
    
