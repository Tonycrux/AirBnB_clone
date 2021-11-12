#!/usr/bin/python3
""" Main class for AirBNB Console """
import cmd

class HBNBCommand(cmd.Cmd):
    """ Console that emulate AirBNB """
    prompt = '(hbnb) '

    def do_quit(self, line):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, line):
        """ EOF execution to exit the program """
        return True

    def emptyline(self):
        """ Empty file """
        pass
        
if __name__ == "__main__":
    HBNBCommand().cmdloop()
