#!/usr/bin/env python
"""lab13_3.py  Implement this inheritance tree:

     Employee
        name

     SalariedEmployee   --> Inherits from Employee
        Has a yearly salary.

     ContractEmployee   --> Inherits from Employee
        Has an hourly rate
"""
from __future__ import division
import sys   

class Employee:
    """Employee class, should only be instantiated in
    a subclass"""

    def __init__(self, name, pay_rate):
        self.name = name
        self.pay_rate = float(pay_rate)

    def GiveRaise(self, percent):
        """percent is the percent raise, where 100 doubles
        the pay rate."""

        percent /= 100.0
        self.pay_rate *= 1 + percent

    def PrintName(self):
        print self.name,

class SalariedEmployee(Employee):
    """pay_rate is the yearly salary.  A pay period is
    1 week."""

    def CalculatePay(self, weeks):
        return self.pay_rate * weeks/52.

class ContractEmployee(Employee):
    """pay_rate is hourly pay.  A pay period is 1 hour."""

    def CalculatePay(self, hours):
        return self.pay_rate * hours

def main():
    joe = SalariedEmployee('Joe', 52000)
    joe.PrintName()
    print "here's $%.2f for you. " % joe.CalculatePay(1) 
    joe.GiveRaise(2)    
    joe.PrintName()
    print "here's $%.2f for you. " % joe.CalculatePay(2) 

    susan = ContractEmployee('Susan', 100)
    susan.PrintName()
    print "here's $%.2f for you. " % susan.CalculatePay(80) 
    susan.GiveRaise(2)     
    susan.PrintName()
    print "here's $%.2f for you. " % susan.CalculatePay(80)

    fred = Employee('Fred', 100)  
    try:
        fred.CalculatePay(20) # Crash! 
    except AttributeError:    # No CalculatePay for Employee
        pass

if __name__ == '__main__':
    main()  # Output given in specification
