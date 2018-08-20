#!/usr/bin/env python
"""Optional: A decorator is a function for wrapping another
function, or many other functions.  Here we are timestamping
the function calls.""" 
import time  

def TimeDecorator(Func):
    """Decorator function for reporting when the function
    was called."""
    def WrappedFunction(*args, **kw_args):
        print "It's %s, time to %s:" % (time.ctime(),
                                         Func.__name__)
        return Func(*args, **kw_args)
    return WrappedFunction

def DoBreakfast(meat='bacon', eggs='scrambled'):
    print "Have some %s and %s eggs.  Enjoy!" % (meat, eggs)

DoBreakfast = TimeDecorator(DoBreakfast) 

@TimeDecorator  # syntax available in 2.5
def DoLunch(**substitutions):
    menu = {'meat':'ham', 'cheese':'american', 'bread':'white'}
    menu.update(substitutions)
    print ("Here's your %(meat)s and %(cheese)s"
           " on %(bread)s bread." % menu)

@TimeDecorator
def DoTea():
    print "Tea time!"

@TimeDecorator
def DoDinner(menu):
    print "%s for dinner tonight." % (menu.title())

def main():
    DoBreakfast(meat='sausage', eggs='basted')
    time.sleep(1)
    DoLunch(cheese='swiss', bread='rye')
    time.sleep(1)
    DoTea()
    time.sleep(1)
    DoDinner('roast beef')

if __name__ == '__main__':
    main()
