#!/usr/bin/env python
""" Write a function that returns a total cost from the 
sales price and sales tax.  The default value for the 
tax rate should be 8.25%.
"""
from __future__ import division

def CalculateCost(price, tax=.0825):
    return price * (1 + tax)

def main():
    print " price |   .0825 |   .0925"
    for price in range(50, 1001, 50):
        dollars = price/100
        print "$%5.2f | $%6.2f | $%6.2f" % (dollars,
                 CalculateCost(dollars), 
                 CalculateCost(tax=.0925, price=dollars))
main()
