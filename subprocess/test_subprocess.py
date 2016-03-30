#! /usr/bin/env python
# -*- conding: utf-8 -*-
import getopt
import os
import subprocess
import sys
import stat
import time
import shutil

BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)

#following from Python cookbook, #475186
def has_colours(stream):
    if not hasattr(stream, "isatty"):
        return False
    if not stream.isatty():
        return False # auto color only on TTYs
    try:
        import curses
        curses.setupterm()
        return curses.tigetnum("colors") > 2
    except:
        # guess false in case of error
        return False
has_colours = has_colours(sys.stdout)


def printout(text, colour=WHITE):
    if has_colours:
       seq = "\x1b[1;%dm" % (30+colour) + text + "\x1b[0m"
       sys.stdout.write(seq)
    else:
       sys.stdout.write(text)


def check_squashfs_tool():
    p=subprocess.Popen("rpm -q squashfs-tools",shell=True,stdout=subprocess.PIPE)
    p.wait()
    sqfs_version=p.stdout.read()
    
    if "4.3-0.20" in sqfs_version:
      print 'squashfs-tool is already'
    else:
      print 'squashfs-tools is not install or version is wrong'
      print 'try \"yum install -y squashfs-tools\"'
      exit(1)
     
if __name__ == '__main__':

  subprocess.call(['ls', '-l'])
  subprocess.call("ls -l", shell=True) 
  check_squashfs_tool()
