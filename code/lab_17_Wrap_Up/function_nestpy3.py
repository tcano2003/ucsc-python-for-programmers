#!/usr/bin/env python3
"""function_nest.py Adapted from 'Learning Python'
by Mark Lutz & Davis Ascher"""  

x = "global x"
y = "global y"

def F1():
    def F2():
        y = "F2's y"
        def F3():
            print ("F3 sees this x =", x) #F3 sees global x
            print ("F3 sees this y =", y) #F3 sees nested namespace and sees F2's y. Finds it within F2. if define class, can point to global
        F3()
    F2()
    print ("F1 sees this x =", x)
    
if __name__ == '__main__':
    F1()
