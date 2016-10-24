#!/usr/bin/env python
#A library of stuff to use

##Import stuff

def hr(s, c='#'):
    #not worth figuring the term width cross-platform, assume 80
    width = 80
    padding = width - 2 - len(s)
    print c.center(padding/2,c) + ' ' + s + ' ' + c.center(padding/2,c)

##Only run if not called by another file/program
if __name__ == "__main__":
    main()

