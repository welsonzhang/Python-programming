#! /usr/bin/env python
# -*- conding: utf-8 -*-

import os
import socket
import fcntl
import struct
import subprocess
import re
import getopt
import sys

def main():
    (prev_pid, next_pid, inputfile) = usage()    
    strace(prev_pid, next_pid, inputfile)

def usage():
    try:
        opts, args = getopt.getopt(sys.argv[1:],"hp:n:i:")
    except getopt.GetoptError as err:
        print 'ERROR:', err
        sys.exit(1)
    prev_pid = ""
    next_pid = ""
    inputfile = ""
    for op, value in opts:
        if op == "-p":
            prev_pid = value
        elif op == "-n":
            next_pid= value
        elif op == "-i":
            inputfile = value
        elif op == "-h":
            print "python trace.py -p <prev_pid> -n <next_pid> -i <inputfile>"
            print "python trace.py -h"

    if prev_pid != "" and next_pid != "":
        return (prev_pid, next_pid, inputfile)
    else:
        sys.exit(1)
    
def strace(prev_pid, next_pid, inputfile):
    f = open(inputfile)
    while True:
        lines = f.readlines(100000)
        if not lines:
            break
        for index, line in enumerate(lines):
            if re.search('pid\='+next_pid, line) and re.search('sched\_wakeup', line):
                prevline_list=line.strip().split(' ')
                prevline_list = filter(lambda a: a != '', prevline_list)
                prevtime = prevline_list[3]
                prevtime = prevtime[0:len(prevtime)-1]
                prevtime_float = float(prevtime)*1000000
                for nextindex in range(index+1, len(lines)):
                    if re.search('prev\_pid\='+prev_pid, lines[nextindex]) and re.search('next\_pid\='+next_pid, lines[nextindex]) and re.search('sched\_switch', lines[nextindex]):
                        nextline_list = lines[nextindex].strip().split(' ')
                        nextline_list = filter(lambda a: a != '', nextline_list)
                        nexttime = nextline_list[3]
                        nexttime = nexttime[0:len(nexttime)-1]
                        nexttime_float = float(nexttime)*1000000
                        print nexttime_float - prevtime_float
                        break
                            
 
 
if __name__ == "__main__":
    main()
