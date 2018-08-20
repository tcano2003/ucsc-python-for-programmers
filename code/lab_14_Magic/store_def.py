#!/usr/bin/env python
"""  

Here we implement the diagram, demonstrating a "contains a" 
or "has a" relationship between classes, and a pseudo-private
attribute and method.  Inheritance is a "is a" relationship.

Below, in PersonnelDept.__init__, notice that there is
self.__welcomers.  This is a "private" attribute because it
has 2 leading underscores and no more than 1 trailing
underscore.  It gets mangled to _PersonnelDept__welcomers
(_ClassName + attribute_name) so that, from outside the class,
__welcomers does not exist.
"""
import welcomer_def   

class Store:
    __number_of_stores = 0

    def __init__(self, name):
        Store.__number_of_stores += 1
        print "Store number %d created." % self.__number_of_stores
        self.name = name
        self.hr = PersonnelDept(self.name) # Store *has a*
                                           # PersonnelDept

class PersonnelDept:
    def __init__(self, name):
        self.__welcomers = [] 
        self.store_name = name

    def Hire(self, name):
        new_guy = welcomer_def.Welcomer(name, 30000)
        self.__welcomers += [new_guy]
        print self.store_name, (
              "welcomes %s, our new welcomer." % new_guy)
        return new_guy

    def __Find(self, name):
        for (i, worker) in enumerate(self.__welcomers):
            if worker.name == name:
                return i
        return -1

    
    def Fire(self, name):
        index = self.__Find(name)
        if index == -1:
            return name, "doesn't work here."
        x = self.__welcomers.pop(index)
        print "%s, you are terminated." % x
        print "Thank you and good luck." 

def main():
    flormart = Store("FlorMart")
    jane = flormart.hr.Hire("Jane")
    jane.Greet()
    print jane, "here's $%.2f for you. " % jane.CalculatePay(2)
    print """Calling Jane("You're in trouble")"""
    print jane, "replies:"
    jane("You're in trouble")
    flormart.hr.Fire("Jane")

if __name__ == "__main__":
    main()
