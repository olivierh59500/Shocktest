#!/usr/bin/env python

import re
import sys

shellsh = {"\(\)\s*\{.+?\};","\(\)\s*\{\s*\(.*\)=>\\\\"}

if len(sys.argv) <= 1:
  exit("Usage: shocktest.py access.log")

else:
  #print sys.argv[1]
  opfile = sys.argv[1]
  try:
    i = open(opfile,'r')
  except:
    exit('There was an error opening the file!')
  for line in i.readlines():
    for pattern in shellsh:
      match = re.findall(pattern,line)
      if match:
        print "Found shellshock pattern!"
        print line
      else:
        continue
  i.close()
