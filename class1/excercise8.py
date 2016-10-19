#!/usr/bin/env python
from ciscoconfparse import CiscoConfParse
import pprint

#find and display parent in config
def printParent(needle,printNeedle=False):
    objects = cisco_cfg.find_objects(needle.encode('string-escape'))
    for i in objects:
        print i.parent.text
        if printNeedle:
            print i.text

#prettify
def hr(s, c='#'):
    #not worth figuring the term width cross-platform, assume 80
    width = 80
    padding = width - 2 - len(s)
    print c.center(padding/2,c) + ' ' + s + ' ' + c.center(padding/2,c)

#Load the cisco cfg
cisco_cfg = CiscoConfParse("cisco_ipsec.txt")

#Find all of the crypto map entries that are using PFS group2
hr('Crypto Maps using PFS group2')
printParent("^ set pfs group2$")

#Using ciscoconfparse find the crypto maps that are not using AES (based-on the transform set name).
hr('crypto maps that are not using AES')
#Print these entries and their corresponding transform set name.
printParent("^ set transform-set (?!AES-SHA)", True)
