#!/usr/bin/env python3
"""Demonstrates the os.walk function, one of many
very useful things given to us in the os module.
"""
import time  
import os 
        
def Process(this_dir, dir_names, file_names):
    print ("In", os.path.abspath(this_dir))
    for node_name in sorted(dir_names + file_names):
        whole_name = os.path.join(this_dir, node_name)
        if os.path.isdir(whole_name):
            print ('    directory:', node_name)
        else:
            print ('    %s:\n        %s' % (
                node_name, time.ctime( 
                os.path.getmtime(whole_name))))

if __name__ == '__main__':
    for (this_dir, dir_names, file_names) in os.walk('cats'):
        Process(this_dir, dir_names, file_names)
