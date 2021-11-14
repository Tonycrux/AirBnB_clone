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
        from ..base_model import BaseModel
        from ..user import User
        from ..state import State
        from ..city import City
        from ..amenity import Amenity
        from ..place import Place
        from ..review import Review

        if exists(self.__file_path):
            with open(self.__file_path) as jsonfile:
                decereal = json.load(jsonfile)
            for keys in decereal.keys():
                if decereal[keys]['__class__'] == "BaseModel":
                    self.__objects[keys] = BaseModel(**decereal[keys])
                elif decereal[keys]['__class__'] == "User":
                    self.__objects[keys] = User(**decereal[keys])
                elif decereal[keys]['__class__'] == "State":
                    self.__objects[keys] = State(**decereal[keys])
                elif decereal[keys]['__class__'] == "City":
                    self.__objects[keys] = City(**decereal[keys])
                elif decereal[keys]['__class__'] == "Amenity":
                    self.__objects[keys] = Amenity(**decereal[keys])
                elif decereal[keys]['__class__'] == "Place":
                    self.__objects[keys] = Place(**decereal[keys])
                elif decereal[keys]['__class__'] == "Review":
                    self.__objects[keys] = Review(**decereal[keys])
