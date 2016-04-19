#! /usr/bin/env python
# -*- conding: utf-8 -*-
import getopt
import os
import sys 
import subprocess
import stat
import time
import shutil
import re
import json
import threading

n():
    filename = 'win.gpt'
    f = open(filename, 'rb')
    f.seek(0, 0)
    index = 0 
    for i in range(0, 16):
        print '%3s' % hex(i),
    print
    for i in range(0, 16):
        print '%-3s' % '#',
    print 
    while True:
        temp = f.read(1)
        if len(temp) == 0:
            break;
        else:
            print "%3s" % temp.encode('hex'),
            index = index + 1
        if index == 16:
            index = 0
            print
    f.close()

if __name__ == "__main__":
    main()
