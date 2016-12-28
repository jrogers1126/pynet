#!/usr/bin/env python

def func3():
    print "Function 3 from the world module"

'''
4. Create a class MyClass in world.py.

    a. This class should require that three variables be passed in upon initialization.
    b. Write two methods associated with this class 'hello' and 'not_hello'. Have both these methods print a statement that uses all three of the initialization variables.
'''

class AdlibClass(object):
    def __init__(self, verb, adjective, noun):
        self.verb = verb
        self.adjective = adjective
        self.noun = noun

    def hello(self):
        print "Johnny said hello to the {} {} as he {}".format(self.adjective, self.noun, self.verb)

    def not_hello(self):
        print "While {} Johnny {}, he looked at the {}".format(self.adjective, self.verb, self.noun)


class NewAdlib(AdlibClass):
    def hello(self):
        print "Johnny dice hablo de la {} {} a el {}".format(self.adjective, self.noun, self.verb)


def main():
    #Write program here
    print "This was NOT called by another program"

##Only run if not called by another file/program
if __name__ == "__main__":
    main()


