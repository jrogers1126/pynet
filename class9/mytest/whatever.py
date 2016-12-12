#!/usr/bin/env python

def func2():
    print "Function 2 from the whatever module"

def main():
    #Write program here
    print "This was NOT called by another program"

##Only run if not called by another file/program
if __name__ == "__main__":
    main()


