#!/usr/bin/python3

"""This is 
"""
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '


    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True
    def do_EOF(self, line):
        """Quit command to exit the program
        """
        return True
    
    def emptyline(self):
        """A Method to do nothing when an empty line is
        entered by the user
        """
        pass



if __name__ == '__main__':
    HBNBCommand().cmdloop()