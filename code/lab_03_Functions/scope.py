#!/usr/bin/env python
"""Global/module-level identifier behavior."""

pies = 1 # global identifier

def DoApple():  
   """alters the local pies, shadows the global identifier"""
   pies = 25 
   print "Apple: local pies in DoApple() is %s." % pies
   pies += 1
   print "Apple ends: local pies = %s" % pies

def DoBerry():
   """assigning the global identifier pies"""
   global pies
   print "Berry: global pies is %s." % pies
   pies *= 10
   print "Berry ends: global pies is %s." % pies 

def DoCherry():
   """referencing the global identifer"""
   print "Cherry: no probem with referencing global pies = %s" % (
       pies)

def DoMud():
   """assigning after reference -- reference doesn't work"""
   print "Mud(): pies = %s" % pies
   pies = 999
  
DoApple()
DoBerry()
DoCherry()
DoMud()
