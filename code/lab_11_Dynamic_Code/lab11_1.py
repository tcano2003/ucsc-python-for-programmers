#!/usr/bin/env python
"""soccer_team.py with getattr and setattr.
"""

import sys 
from soccer_team import NotifyForwards, NotifyDefenders, NotifyMidfielders, NotifyGoalies 

this_module = sys.modules[__name__]

def ProcessTeam(stream):
    position_strs = []
    for line in stream:
        line = line.strip()
        if not line:
            continue
        if line.endswith(":"):
            position = line[:-1]
            setattr(this_module, position, [])
            position_strs += [position]
            continue
        details = line.split(" ", 1)
        setattr(this_module, position,
                getattr(this_module, position) + [details])
        print "Yeh %s #%s " % (details[1], details[0])\
                + getattr(this_module, "Notify%s" % position)()
    return stream.name, position_strs

def PrintTeam(team_name, position_strs):
    print team_name + ":"
    for each in position_strs:
        print "  %s:" % each
        for player in sorted(getattr(this_module, each)):
            print "    " + ": ".join(player)

def main(team_name = "Bees"):
    team_name, position_strs = ProcessTeam(open(team_name))
    PrintTeam(team_name, position_strs)
    print "\nThe %s data file:" % (team_name)
    sys.stdout.write(open(team_name).read())

if __name__ == "__main__":
    main()

