from ccparser import *
from commands import *

while True:
   try:
      # parse the command
      parser = Parser(input("Capsian$ "))
      # get the tree
      tree = parser.parse()
      
      # organize ..
      command = tree[0] # .. the class
      sub_command = tree[1] # .. the method
      args = tree[2] # .. the function args

      # there isn't a key eq to command in the commands dictionary ?
      if not command_table.keys().__contains__(command):
         error(f"a class named {command} does not exist")

      # load the class from the dictionary
      entry = command_table[command]
      
      # there isn't a key eq to sub_command in entry ?
      if not entry.keys().__contains__(sub_command):
         error(f"no declaration for a method named {sub_command} in the class {command}")
      
      # load the method from the class
      ptr = entry[sub_command](args)
   except KeyboardInterrupt:
      # catch ctrl + c
      print("system close")
   except CCError as e:
      # some errors in the process? let's report it
      print("Error:", e)