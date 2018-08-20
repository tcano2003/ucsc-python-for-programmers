#!/usr/bin/env python
"lab19_2.py - gives a raise to everyone in the address.data file."
import re

salary_finder = re.compile(r"(?P<salary>\d+)$",
                           re.VERBOSE | re.MULTILINE)

def GiveRaise(amount, text):
    """Gives a raise to the salaries in the text"""
    def UpIt(match_object):
        return str(int(match_object.group("salary")) + amount)
    return salary_finder.sub(UpIt, text)

def main():
    import norma
    print GiveRaise(250, norma.ReadFile('address.data'))

if __name__ == '__main__':
    main()

