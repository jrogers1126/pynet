#!/usr/bin/env python
## Read in stuff from files
import yaml, json, pprint

# read from the YAML file
with open("week1.yaml") as f:
    y = yaml.load(f)

# read from the JSON file
with open("week1.json") as f:
    j = json.load(f)

#pprint both 
print '#'.center(37, '#') + ' YAML ' + '#'.center(37, '#')
pprint.pprint(y)
print
print '#'.center(37, '#') + ' JSON ' + '#'.center(37, '#')
pprint.pprint(j)

