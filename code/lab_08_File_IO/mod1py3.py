#!/usr/bin/env python3 
"""You can use ->   from module import *
   to bring all the attributes into your local namespace.
   But this is usually considered to be bad practice.
   You lose track of which attributes are local and are
   not local.  And, here's another problem.
"""

immutable = 1   
mutable = [1, 2, 3]    

def PrintImmutable():
    print (immutable)

def PrintMutable():
    print (mutable)
