#!/usr/bin/env python3
"""Function with many arguments and many return values."""

def Analyze(one, other):       
    total = sum((one, other)) # sum demands a sequence
    average = total/2.0       # min and max are flexible
    return min(one, other), max((one, other)), total, average 

def Print(min_number, max_number, total, average):
    print ("min_number=", min_number, end=' ')
    print ("max_number=", max_number, end=' ')
    print ("total=", total, end=' ')
    print ("average=", average)
    print ()

def main():
    min_number, max_number, total, average = Analyze(1, 8)
    Print(min_number, max_number, total, average)

    answer = Analyze(100, 50)
    min_number, max_number, total, average = answer
    Print(min_number, max_number, total, average)

    Print(*Analyze(3.2, 8.7))  # We'll study this later.

main()

