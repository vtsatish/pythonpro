import os
from os import path

def fileExists(filepath):
   """This program returns true if a file exists"""

   existBool = path.exists(filepath)
   print("Item exists:" + str(existBool))
   return existBool