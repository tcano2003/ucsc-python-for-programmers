#!/usr/bin/env python3
"""Here is a very simple object-oriented python program.
Note that we make 3 namespaces: the Greeter class, and two
instances of the Greeter class, fred and alma.""" 

class Greeter:   
    """The Greeter class makes Greeter objects that can
    greet you."""

    def Greet(self):         # 'self' is always the first 
        print ('Hello World')# argument of every method in 
                             # every class.
def main():                  # 
    fred = Greeter()         # A call:  fred.Greet() is 
    print ('fred.Greet():')  # interpreted as 
    fred.Greet()             # Greeter.Greet(fred). So the
    alma = Greeter()         # greeter object labeled 
    print ('alma.Greet():')  # 'fred' is the namespace we 
    alma.Greet()             # are relabeling as 'self'

    PrintStringValue(fred=fred, alma=alma, Greeter=Greeter) #identifier is label (fred=Greeter(fred)). It is a dictionary

def PrintStringValue(**dict_version):
    for namespace_string in dict_version:
        print (namespace_string, ':', end='')
        print (dict_version[namespace_string])

if __name__ == '__main__':
    main()

