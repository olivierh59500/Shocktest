#!/usr/bin/env python

import re
import sys

shellsh = {"\(\)\s*\{.+?\};","\(\)\s*\{\s*\(.*\)=>\\\\"}

if len(sys.argv) <= 1:
  exit("Usage: shocktest.py access.log")

else:
  #print sys.argv[1]
  opfile = sys.argv[1]
  svfile = raw_input("Save contents if found? [y/n]: ")
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
