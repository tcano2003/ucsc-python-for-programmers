#!/usr/bin/env python3
"""manynames.py -- adapted from "Learning Python" by Mark Lutz
and David Ascher, published by O'Reilly.  Demonstrates name-spaces 
associated with classes, functions, and methods.""" 

x = 11                # Module (global) name/attribute

class C:
    x = 22            # Class attribute
    def M(self):
        print (x)       # Sees the global x
        self.x = 44   # instance attribute

def F():
    x = 55        # Local identifier in function

def G():
    print (x)       # Access module x (11)

if __name__ == '__main__':
    obj = C()
    obj.M()       # 11: sees the global x
    print (obj.x)   # 44: instance
    print (C.x)     # 22: class (obj.x if no x in instance)
    print (x)       # 11: module (manynames.x outside file)
    G()           # 11: sees the global x
    try:
        print (F.x)    # fails: only visible in function
    except AttributeError as e:
        print ("F.x failed:", e)
