#!/Users/dag/Envs/countingsocial/bin/python
import time, argparse 
import os, sys

def main(argv):
  """
  takes command line arguments, and makes a new python package at (path) 
  Optionally takes an argument -m, which adds a docstring to the __init__.py

  """
  
  directory = ""
  message = "# Created on " + time.strftime("%d/%m/%Y")
  parser = argparse.ArgumentParser()
  help = "Make a new python package with an optional -m 'message' in the docstring"
  parser.add_argument("directory", help=help, type=str)
  parser.add_argument("-m", help="optional message string")
  args = parser.parse_args()

  print args.m
  directory = args.directory
  if directory == 'None':
    print "No arguments supplied.  Usage 'mkpkg [path] (optional) -m 'message'"
    sys.exit(2)
    return False
  directory = argv[0]

  try:
    os.mkdir(directory)
  except:
    print "The directory '"+ directory + "' already exists."
    sys.exit(2)
    return

  if args.m != None:
    message = message + "\n" + "\"\"\""+ args.m + "\"\"\""

  f = open(os.path.join(directory,"__init__.py"), 'w+')
  f.write(message)
  f.close()
   
if __name__ == "__main__":
  main(sys.argv[1:])
