#!/usr/bin/env python3
"""Write a function that returns a total cost from the 
sales price and sales tax.  The default value for the 
tax rate should be 8.25%"""
from __future__ import division

def CalculateCost (sales_price, sales_tax = .0825):
    return sales_price * (1 + sales_tax)

def main():
    print (" price |   .0825 |   .0925")
    for sales_price in range (50, 1001, 50):
        dollars = sales_price/100
        print ("$%5.2f | $%6.2f | $%6.2f" % (dollars,
               CalculateCost(dollars),
               CalculateCost(sales_tax=.0925, sales_price=dollars)))
main()
