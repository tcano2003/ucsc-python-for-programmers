#!/usr/bin/env python3
"""Alternatively, we define an __init__ method so that the
name is given when the object is created."""
  
class Greeter:
    # This Greeter class needs a name when instantiated.

    def __init__(self, name): # (self is called automatically)
        # __init__ is Python's constructor method
        self.name = name

    def Greet(self): #always use self
        print ("Hello World. I'm", self.name)

def main():
    fred = Greeter('Fred') # magic init gets called here
    print ('fred.Greet():')
    fred.Greet()

    x = Greeter()    #  error!

if __name__ == '__main__':
    main()

