#!/usr/bin/env python

def func1():
    return "Function 1 from the {} module".format(__name__)

def main():
    #Write program here
    print "This was NOT called by another program"

##Only run if not called by another file/program
if __name__ == "__main__":
    main()


