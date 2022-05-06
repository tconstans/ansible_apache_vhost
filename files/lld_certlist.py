#!/usr/bin/python3
import json
import os
import re

import sys

if __name__ == "__main__":
  data=[]
  filelist = os.listdir( '/etc/letsencrypt/live/' )
  cert=[]
  r=re.compile("(README|.*-[0-9]{4}$)")
  certs = list(filter(r.match, filelist ))
  for line in filelist:
    if line == "README": continue
    if re.search( ".*ORIG$", line) : continue
    if re.search( ".*-[0-9]{4}$", line) : continue
    cert.append( line )
	 
  data = [{"{#CERT}": line.strip()} for line in set(cert)]
  print(json.dumps({"data": data}, indent=4))

