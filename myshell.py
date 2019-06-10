
from os import system, name
import subprocess
import os
import sys
import cmd
import msvcrt
from time import sleep

class Shell(cmd.Cmd):
   """Simple command processor example."""
   """Tested using Windows operating System"""
   
   print("To access the help menu please type help")
   
      
      
   #Dummy function to greet the person that it's using the program.
   def do_greet(self, person):
       """greet [person] Greet the named person"""
       if person:
          print ("Hi, ", person)
       else:
          print ('Hi')

          
   def do_clear(self,name):
      ###clear the screen using the os module
      """clear [self] clear the screen"""
      # for windows """
      command = "cls"
      subprocess.call(command,shell = True)
      
   
   def do_chdir(self,directory):
      """ chdir < directory > Changing working directory to a new one.
      If chdir is followed by no argument  it will remain at current working directory"""
      #The current path of the working directory
      path  = os.getcwd()
      print("Current working directory is " + path)
      #If there no new directory,it will stay in the same path.
      if directory == "":
	      os.chdir(path)
      # Else it will change  to the new directory.	  
      try:
	      os.chdir(directory)
      except FileNotFoundError:
         print("The system cannot find the path specified.")
      
	      
      
      # Printing the current working directory to check if any change has been made
      print("Current working directory is " , os.getcwd())
   def do_dir(self,path):
      """ dir <self> Displaying all the files in the current working directory."""
      # Getting the path of the directory where the Shell is stored.
      path = os.getcwd()
      
 
      files = os.listdir(path)
      # Listing all the files from the directory that the shell is stored.
      for name in files:
         print(name)

         
   def do_echo(self,echo):
      """Displays messages or turns on or off the command echoing feature. If used without parameters, echo displays the current echo setting."""
      
      if echo == "":
         print("ECHO is on")
         #new line
         print()
      else:
         print(echo)
         #new line
         print()
   def do_environ(self,env):
      "List all the enviroment variables."
      # listing all the enviroment variables using a dictionary.
      # The keys will contatin the values.
      for line in os.environ.keys():
         print(line ,os.environ[line])

   def do_pause(self,pause):
      # An infinite loop that only the key enter will stop it.
      # Done with the msvcrt module from the windows module that will read in the key.
      """Pause, it will pause the shell untill enter key will be pressed.No other key  but enter will resume the shell"""
      print("Press enter to continue.  .  .")
      read = msvcrt.getch()
      # b'\r' is the code for the enter key which will allow to unblock the loop
      while read != b'\r':
         read = msvcrt.getch()
         continue

      
   def do_quit(self, args):
      # the quit command will quit the shell
      """Quits the program."""
      print ("Quiting!")
      raise SystemExit

   
   def do_EOF(self,arg):
      #Allowing for IO redirection
      # Checks for end of file
      #returns when end of file is reached
      return True
  
      
      
			
	
    
   

if __name__ == '__main__':
    prompt = Shell()
    path = os.getcwd()
    prompt.prompt = path  + ">"
    prompt.cmdloop("Starting prompt. . .")
    
