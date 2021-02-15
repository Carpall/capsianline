from os import system

# args when are used, else _

# function pointers
def system_echo(args):
   for arg in args:
      print(arg, end="")

def system_clear(_):
   system("cls")

def system_close(_):
   exit(0)

def system_exec(args):
   for arg in args:
      exec(arg)

# all commands are here
# table
command_table = { 
   # classes
   "system": {
      # methods
      "echo": system_echo,
      "clear": system_clear,
      "close": system_close,
      "exec": system_exec
   }
}