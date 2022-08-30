from cmd import Cmd
import os

class MyPrompmt(Cmd):
    prompt = 'pb> '
    intro = "Welcome! Type ? to list commands"
    def do_exit(self, inp):
        '''Exit the application'''
        print("Bye")
        return True

    def help_exit(self):
        print('Exit the application. Shorthand: x q Ctrl-D.')

    def do_add(self,inp):
        '''Custom shell command for adding two numbers separated by space and providing the result'''
        a, b = inp.split()
        sum = float(a) + float(b)
        print("sum of {} and {} equals: {}".format(a,b,sum))

    def help_add(self):
        print("Sum two numbers that are after the add command. E.g., 'add 1 2' will give 3")

    def do_list(self,inp):
       '''Custom shell command for listing the contents of the current directory'''
       contents = os.listdir(os.getcwd())
       for file in contents:
            print(file)

    def help_list(self):
        print('Lists the contents of the current directory')
 
    do_EOF = do_exit
    help_EOF = help_exit


if __name__ == '__main__':
    MyPrompmt().cmdloop()

