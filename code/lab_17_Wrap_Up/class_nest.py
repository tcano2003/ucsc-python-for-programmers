#!/usr/bin/env python
"""class_nest.py class nesting scopes in the other
direction."""
w = 10   
class C1:   
    x = 99
    class C2:
        y = 100
        class C3:
            z = 101      # <-- Visible from outside
            print w
            print z
            # print C1.x   <-- Can't see outer classes
            # print y          or any outer identifiers
                               # during first read.
if __name__ == '__main__':
    print 'About to initialize:'
    c1 = C1()
