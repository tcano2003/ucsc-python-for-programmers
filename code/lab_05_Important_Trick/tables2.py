#!/usr/bin/env python3
"""Interactive 2-D string unwrapper.
"""
import tablespy3

def main():
    while True:
        response = input("Say something: ")
        if not response:
            break
        words = response.split()
        tables3.PrintTable(words)

if __name__ == '__main__':
    main() 
