#!/usr/bin/env python

##Import stuff
#     a. Make sure that you have PySNMP and Paramiko installed in the lab (i.e. enter the Python shell and test 'import pysnmp', and 'import paramiko').
import pysnmp, paramiko

#     b. Determine which version of PySNMP and Paramiko are installed.  dir(pysnmp) and dir(paramiko) should be helpful here.
print "pysnmp version: " + pysnmp.__version__
print "paramiko version: " + paramiko.__version__ 

#    c. Write a simple Python module that contains one function that prints 'hello' (module name = my_func.py). Do a test where you import my_func into a new Python script. 
from my_func import my_func

def main():
    #Write program here
    my_func()

##Only run if not called by another file/program
if __name__ == "__main__":
    main()


