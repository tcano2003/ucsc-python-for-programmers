#!/usr/bin/env python
"""
Another inheritance example, using the previous examples
by importing the old code.  This one implements __call__,
__str__, and __del__ and a class attribute."""

import sys, os
sys.path.insert(0, os.path.join(os.path.split(__file__)[0], ".."))

import lab_13_OOP.lab13_3 as employee_def   
import lab_13_OOP.greeter5_def as greeter_def 
     
class Welcomer(greeter_def.NamedGreeter,
               employee_def.SalariedEmployee):
    """Inherits from Salaried Employee"""
    welcomers = 0

    def __init__(self, name, pay_rate):
        Welcomer.welcomers += 1
        employee_def.SalariedEmployee.__init__(self, name, 
                                               pay_rate)

    def __call__(self, something): 
        print something, "yourself!"

    def __del__(self):
        Welcomer.welcomers -= 1
        print self, 'says "Oh no!"'

    def __str__(self):
        return self.name

def main():
    Joe = Welcomer("Joe", 20000) # style-guide anxiety here!
    Joe.Greet()
    print Joe, "here's $%.2f for you. " % Joe.CalculatePay(80)
    print
    marsha = Welcomer("Marsha", 19500)
    marsha("Get to work")
    print
    print marsha, "here's $%.2f for you. " % (
        marsha.CalculatePay(80))
    print
    print "There are %d welcomers." % Welcomer.welcomers
    Joe("Goodbye")
    print "Deleting Joe"
    del Joe
    print "There are %d welcomers." % Welcomer.welcomers
    print    
    marsha.Greet()
    print "marsha is going out of scope so runs through del."

if __name__ == "__main__":
    main()
