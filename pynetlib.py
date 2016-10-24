#!/usr/bin/env python
__author__ = "Josh Rogers"
__credits__ = ["Josh Rogers"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Josh Rogers"
__email__ = "2016@tybox.net"
__status__ = "Prototype"

##Import stuff

def hr(s, c='#'):
    #not worth figuring the term width cross-platform, assume 80
    width = 80
    padding = width - 2 - len(s)
    print c.center(padding/2,c) + ' ' + s + ' ' + c.center(padding/2,c)

##Only run if not called by another file/program
if __name__ == "__main__":
    main()

