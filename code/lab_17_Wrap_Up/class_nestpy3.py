#!/usr/bin/env python3
"""class_nest.py class nesting scopes in the other
direction."""
w = 10   
class C1:   #sets x at readtime
    x = 99
    class C2:
        y = 100
        class C3: #sets z at readtime
            z = 101      # <-- Visible from outside
            print (w) #gives global = 10
            print (z) #gives local = 101
            # print C1.x   <-- Can't see outer classes
            # print y          or any outer identifiers
                               # during first read.
if __name__ == '__main__':
    print ('About to initialize:') # x,y,z were set at readtime, before an instance was instantiated
    c1 = C1()
