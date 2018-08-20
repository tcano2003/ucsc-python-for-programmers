#!/usr/bin/env python
"""function_nest.py Adapted from 'Learning Python'
by Mark Lutz & Davis Ascher"""  

x = "global x"
y = "global y"

def F1():
    def F2():
        y = "F2's y"
        def F3():
            print "F3 sees this x =", x 
            print "F3 sees this y =", y
        F3()
    F2()
    print "F1 sees this x =", x
    
if __name__ == '__main__':
    F1()
