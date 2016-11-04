#!/usr/bin/env python
#A library of stuff to use

#import stuff
from pysnmp.entity.rfc3413.oneliner import cmdgen

def horizontal_rule(msg, character='#'):
    #not worth figuring the term width cross-platform, assume 80
    width = 80
    print " {} ".format(msg.strip()).center(width, character)

##Only run if not called by another file/program
if __name__ == "__main__":
    main()

