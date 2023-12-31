#!/usr/bin/python3
"""Module for the entry point of the command interpreter."""

import cmd
from models.base_model import BaseModel
from models import storage
import re
import json

class HBNBCommand(cmd.cmd):
    """class for the command interpreter"""

    prompt = "(hbnb) "
    
    def do_EOF(self, line):
        """Handles End Of File character.
        """
        print()
        return True

    def do_quit(self, line):
        """Exits the program.
        """
        return True

    def emptyline(self):
        """Doesn't do anything on ENTER.
        """
        pass

    if __name__ == '__main__':
    HBNBCommand().cmdloop()
