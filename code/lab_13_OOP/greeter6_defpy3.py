#!/usr/bin/env python3
"""Here we implement another class, a HipGreeter, and have it  
further down the inheritance tree.""" 

class Greeter:                            #   --------------
    def Greet(self):                      #  |              |
        print ("Hello World")               #  | Greeter      |
    def Bye(self):                        #  |              |
        print ("Bye now.")                  #   --------------
                                          #         /|\
class NamedGreeter(Greeter):              #          |
    def __init__(self, name):             #   --------------
        self.name = name                  #  |              |
    def Greet(self):                      #  | NamedGreeter |
        Greeter.Greet(self)               #  |              |
        print ("I'm", self.name)            #   --------------
                                          #         /|\ 
class HipGreeter(NamedGreeter):           #          |
    def Greet(self):                      #   --------------
        NamedGreeter.Greet(self)          #  |              |
        print ("Wazzup.")                   #  | HipGreeter   |
                                          #  |              |
def main():                               #   --------------
    rocky = HipGreeter("Rocky")
    rocky.Greet()
    rocky.Bye()

if __name__ == '__main__':
    main()

