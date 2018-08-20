#!/usr/bin/env python
"""lab12_4.py (Optional) A logging lotto facility."""
import time
import random

LOG_FILE = 'lotto.log'

def LogIt(Func):
    """Decorator function for logging output from the Func."""
    def LoggedFunction(*t_args, **kw_args):
        f = open(LOG_FILE, "a")
        got = Func(*t_args, **kw_args)
        f.write("%s  -> %s:%s\n" % (time.ctime(),
                                    Func.__name__, got))
        f.close()
        return got
    return LoggedFunction

@LogIt
def Lotto():
    return random.sample(xrange(1, 53), 6)

def PrintLotto(the_pick):
    print ", ".join([str(x) for x in the_pick])

def main():
    PrintLotto(Lotto())
    PrintLotto(Lotto())

if __name__ == '__main__':
    main()

