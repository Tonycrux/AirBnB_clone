#!/usr/bin/python3
""" Main class for AirBNB Console """
import cmd
from models import storage
from models.engine import file_storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """ Console that emulate AirBNB """
    prompt = '(hbnb) '
    classes = {"BaseModel", "User"}
    def do_quit(self, line):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, line):
        """ EOF execution to exit the program """
        return True

    def emptyline(self):
        """ Empty file """
        pass

    def do_create(self, line):
        """ Create object and save to storage """
        if line is None or line  == "":
            print("** class name missing **")
        else:
            if line:
                new_obj_id = eval(line + '()')
                new_obj_id.save()
                print(new_obj_id.id)
            else:
                print("** class doesn't exist **")
            
if __name__ == "__main__":
    HBNBCommand().cmdloop()
