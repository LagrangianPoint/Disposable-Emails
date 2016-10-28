#!/usr/bin/python

from pprint import pprint
import sys
import yaml
import json

"""
Cleans a messy input file, removes white space, remove diplicate emails, generates YAML and JSON files.
Stores output in disposable-emails.txt 
"""

if len(sys.argv) == 1:
	print "Missing input file"
	sys.exit(1)

with open(sys.argv[1], 'r') as fh:
	raw = fh.read()


listRaw = raw.split("\n")
setClean = set()
for x in listRaw:
	x = x.strip()
	if x != "":
		setClean.add(x)

listClean = list(setClean)
listClean = sorted(listClean)

pprint(listClean)
dictDisposable = {"disposable-emails" : listClean}

with open('disposable-emails.yaml', 'w') as fh:
	yaml.dump(dictDisposable, fh,  default_flow_style=False)



strJSON = json.dumps(dictDisposable, separators=(",\n",':'))

with open('disposable-emails.json', 'w') as fh:
	fh.write(strJSON)

strOut = "\n".join(listClean)
with open('disposable-emails.txt', 'w') as fh:
	fh.write(strOut)
	
