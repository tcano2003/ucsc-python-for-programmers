#!/usr/bin/env python3
"""Classes are blueprints for name spaces.  Attributes
can be added on an object by object basis.  Feature or
flaw?"""   

class NameSpace:

    def __init__(self):
        self.attribute = 10 #one attribute for self

    def __str__(self):
        return str(self.__dict__) #return as a dictionary

def main():
    george = NameSpace()
    george.age = '44'
    george.job = 'coder'

    dinner = NameSpace()
    dinner.maindish = 'stew'
    dinner.dessert = 'pie'
    #dinner.attrbute = '101' # attribute is misspelled, returns no errors!!
    dinner.attribute = '101'

    print (george)
    print (dinner)

if __name__ == '__main__':
    main()
