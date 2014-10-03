#!/usr/bin/env python


#Python script to try and find shellshock attempts in logs or files
#Please feel free to modify the script and use it.
#
#As usual, my idea here is to make it simple.
#
#Author: NinjaSl0th
#Twitter: @ninjasl0th

import re
import sys

#Store the different shellshock regular expressions
shellsh = {"\(\)\s*\{.+?\};","\(\)\s*\{\s*\(.*\)=>\\\\"}

if len(sys.argv) <= 1:
  exit("Usage: shocktest.py access.log")

else:
  opfile = sys.argv[1]
  svfile = raw_input("Save contents if found? [y/n]: ")
  #some error checking when opening the file
  try:
    i = open(opfile,'r')
  except:
    exit('There was an error opening the file!')
  for line in i.readlines():
    for pattern in shellsh:
      match = re.findall(pattern,line)
      if match:
        print line
        if svfile == "y" or svfile == "Y":
          a = open("ShocksFound.txt",'a')
          a.write(line+'\n')
          a.close()
        else:
          pass
      else:
        continue
  i.close()
