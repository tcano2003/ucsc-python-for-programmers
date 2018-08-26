#!/usr/bin/env python3
"""Here we implement 'inheritance'      --------------
to leave the original Greeter class    |              |
intact and add a NamedGreeter class,   | Greeter      |
that has all the functionality of      |              |
the Greeter class plus some new         --------------
things.                                      /|\
                                              |
                                        --------------
                                       |              |
                                       | NamedGreeter |
                                       |              |
                                       ---------------    """
class Greeter: 

    def Greet(self):
        print ("Hello World")

class NamedGreeter(Greeter):
    # Inherits the methods in the Greeter class, and adds some
    # of its own.

    def __init__(self, name):
        self.name = name

    def SayMyName(self):
        print ("I'm", self.name)

def main():
    fred = NamedGreeter('Fred')
    print ('fred.Greet():')
    fred.Greet()
    fred.SayMyName()

    # code that depends on the Greeter class is unaffected.
    x = Greeter()
    print ('x.Greet():')
    x.Greet()

if __name__ == '__main__':
    main()
