#!/usr/bin/env python

import subprocess



def main():
    p = subprocess.Popen("ps -eo comm,pcpu",shell=True,stdout=subprocess.PIPE)
    p.wait()
    output = p.stdout.read().strip()
    array = output.split()
    ret = array[2:]
    for i, txt in enumerate(ret):
        if i%2 == 1:
            if float(txt) > 10:
                print ret[i-1]


if __name__=="__main__":
    main()
