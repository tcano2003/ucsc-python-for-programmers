#!/usr/bin/env python3
"""lab14_3.py  A Clock class\n
an example of unit testing"""

import time

class Clock:
    """Clock() for now, or Clock(hours, minutes) or Clock(minutes)
    or Clock("1:20") or Clock(dict) where dict has keys
    'hours' and 'minutes'."""

    def __init__(self, *args, **dict_args): # google style guide says no ** in dict_args
        no_args = len(args)
        if dict_args:
            self.__ResolveDictArgs(dict_args) #call private method Resolve...
        elif no_args <= 1: # If only 0 or 1
            if no_args == 0: # if zero args
                # making args[0] Now
                args = [time.ctime()[11:16]]
            if isinstance(args[0], str):
                self.hours, self.minutes = args[0].split(':')
            elif isinstance(args[0], dict): #if it is a dict, call the private ResolveDictArgs()
                self.__ResolveDictArgs(args[0]) # try as a tuple
            else:  # sequence or single value
                try:
                    self.hours, self.minutes = args[0]
                except TypeError as e:
                    self.hours = 0
                    self.minutes = args[0]
        elif no_args == 2:
            self.hours, self.minutes = args #if 2 args, hours and minutes
#        else:
#            raise TypeError as e2, Clock.__doc__: #__doc__ magic doc can be used
#                Clock.__doc__
        self.__Normalize() #private method, this method means put back on the clock

    def __add__(self, other):
        return Clock(self.hours + other.hours, self.minutes + other.minutes)

    def __cmp__(self, other):
# deprecated in Python 3        return cmp(int(self), int(other))
        return cmp(int(self), int(other)) #----------------------------FIX THIS---------------------

    def __eq__(self, other): #magic equals __eq__. compare them, if equal, True. Need an int to compare.
# deprecated in Python 3 if cmp(self, other) == 0:
        if ((self > other) - (self < other)) == 0:
            return True
        return False

    def __int__(self):
        return self.MinutesSince12()

    def MinutesSince12(self):
        return (self.hours % 12) * 60 + self.minutes

    def __neg__(self):
        return Clock(-self.hours, -self.minutes)

    def __Normalize(self):
        """Assumes that self.minutes and self.hours are floatable 
        and makes the values be ints on a clock.
        """
        self.minutes = float(self.minutes) + (float(self.hours)
                                      - int(self.hours)) * 60
        self.minutes = int(round(self.minutes))
        self.hours = int(self.hours) + self.minutes//60
        self.minutes %= 60
        self.hours = 1 + (self.hours - 1) % 12

    def __repr__(self): # should return a string. If execute the string, should get same object back. result: "Clock('2:30')"
        return self.__class__.__name__ + """('%s')""" % (self)

    def __ResolveDictArgs(self, dict_args):
        try:
            self.minutes = dict_args['minutes']
            self.hours = dict_args['hours']
        except:
            pass
#        except KeyError:
#            raise TypeError as e3, Clock.__doc__

    def __str__(self): #gives the time. result: '2:30'
        return "%2d:%02d" % (self.hours, self.minutes)

    def __sub__(self, other):
        return Clock(hours=self.hours - other.hours,
                     minutes=self.minutes - other.minutes)

def main():
    Clock()
    c1 = Clock(12, 59)
    for hours in range(-2, 25, 2): # start at -2, go up to 24 and increase by 2
        for minutes in range(-10, 10):
            c2 = Clock(hours, minutes)
            assert eval(repr(c2)) == c2, "eval, repr error" #assert statement to ensure what we have is what we have. don't use to check user. Asset statements only for developers, ignored in production code (eval and repr are inverse of each other)
            # repr depends on str so
            # both are tested
            cmp_value = int(c2)
            assert Clock(int(c2)) == c2, "int not right: %s" % c2
            c_sum = c1 + c2
            c_diff = c1 - c2
            c3 = c_sum + c_diff # should be 2 * c1
            c4 = Clock(2* c1.hours, 2 * c1.minutes) # new clock that is double of original clock
            assert c3 == c4, "+/-/== error: %s +/- %s" % (c1, c2) # checking clock math
            c5 = -c2
            assert c_diff == c1 + c5
    hours, minutes = 2, 30 #testing __init__ (instantiator, magic init)
    clocks = [Clock(hours, minutes)]
    clocks += [Clock((hours, minutes))]
    clocks += [Clock("%d:%2d" % (hours, minutes))]
    clocks += [Clock({'hours': hours, 'minutes': minutes})] #keywordd args
    clocks += [Clock(hours=hours, minutes=minutes)]
    for each in clocks[1:]:
        assert clocks[0] == each
    try:
        Clock(1, 2, 3)
    except TypeError:
        pass
    else:
        print ("Clock(1, 2, 3) failed to raise an error")

if __name__ == '__main__':
    main()

