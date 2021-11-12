""" Init File Models """
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

storage = FileStorage()
storage.reload()

class Classes(dict):
    """classes"""

    def __getitem__(self, key):
        """get item"""
        try:
            return super(Classes, self).__getitem__(key)
        except Exception as e:
            raise Exception("** class doesn't exist **")


models = [BaseModel]
classes = Classes(**{x.__name__: x for x in models})
