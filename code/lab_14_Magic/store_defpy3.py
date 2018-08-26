#!/usr/bin/env python3
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
import welcomer_defpy3 as welcomer_def  

class Store:
    __number_of_stores = 0 #__means pseudo-private

    def __init__(self, name):
        Store.__number_of_stores += 1 # can also put __number_of_stores_ but __number_of_stores__ would no longer be private
        print ("Store number %d created." % self.__number_of_stores) # referencing...(self,could be store to be more explicit BUT don't publish that code)
        self.name = name
        self.hr = PersonnelDept(self.name) # Store *has a* #just initialize with the self so it has easy access to the entire store
                                           # PersonnelDept

class PersonnelDept:
    def __init__(self, name):
        self.__welcomers = [] #__ private list
        self.store_name = name

    def Hire(self, name):
        new_guy = welcomer_def.Welcomer(name, 30000)
        self.__welcomers += [new_guy] # add the person
        print (self.store_name, ("welcomes %s, our new welcomer." % new_guy)) #announces the person
        return new_guy # returning the object

    def __Find(self, name): #__ private find
        for (i, worker) in enumerate(self.__welcomers):
            if worker.name == name: #if find name, return the index
                return i
        return -1 # if not returns an index, -1

    
    def Fire(self, name):
        index = self.__Find(name) #find in list of welcomers
        if index == -1: # if do not find
            return name, "doesn't work here."
        x = self.__welcomers.pop(index) # the information is removed
        print ("%s, you are terminated." % x)
        print ("Thank you and good luck.")

def main():
    flormart = Store("FlorMart") #
    jane = flormart.hr.Hire("Jane") #hire Jane
    jane.Greet()
    print (jane, "here's $%.2f for you. " % jane.CalculatePay(2)) #Calculate pay for two weeks
    print ("""Calling Jane("You're in trouble")""")
    print (jane, "replies:")
    jane("You're in trouble")
    flormart.hr.Fire("Jane")

if __name__ == "__main__":
    main()
