#!/usr/bin/env python
"""Processing team data using exec and eval."""
import sys
def NotifyForwards(): 
    return "Go for the goal!" 
def NotifyDefenders():
    return "Block that kick!"
def NotifyMidfielders():
    return "Get that ball!"
def NotifyGoalies():
    return "Guard the goal!"

def ProcessTeam(stream):
    position_strs = []
    for line in stream:
        line = line.strip()
        if not line:
            continue
        if line.endswith(':'):
            position = line[:-1]
            exec "%s = []" % (position) in globals()
            position_strs += [position]
            continue
        details = line.split(' ', 1)
        exec "%s += [details]" % (position)
        exec "print 'Yeh %s #%s ' + Notify%s()" % (
            details[1], details[0], position)
    return stream.name, position_strs

def PrintTeam(team_name, position_strs):
    print '\n%s:' % team_name 
    for each in position_strs:
        print '  %s:' % each
        for player in sorted(eval(each)):
            print '    ' + ': '.join(player)

def main(team_name = "Bees"):
    team_name, position_strs = ProcessTeam(open(team_name))
    PrintTeam(team_name, position_strs)
    print "\nThe %s data file:" % (team_name)
    sys.stdout.write(open(team_name).read())

main()
