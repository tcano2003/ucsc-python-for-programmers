#!/usr/bin/env python3
""" 
Get info about your caught exception from sys and traceback
modules."""

import sys      
import traceback  
                     
def Fun():    
    raise ArithmeticError ("Fake message.")

if __name__ == '__main__':
    try:
        Fun()
    except:
        print ('sys.exc_type =', sys.exc_type) #type
        print ('sys.exc_value =', sys.exc_value) #value
        print ('sys.exc_traceback =', sys.exc_traceback) #exception object
        print ("---")
        print (traceback.format_exc(sys.exc_traceback), end='') #can ask traceback module to format the last traceback exception
        print ("---")

