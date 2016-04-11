# encoding: UTF-8
import threading
import time

def context(tJoin):
    print 'in threadContext.'
    tJoin.start()
    tJoin.join()
    print 'out threadContext.'

def join():
    print 'in threadJoin.'
    time.sleep(1)
    print 'out threadJoin.'

tJoin = threading.Thread(target=join)
tContext = threading.Thread(target=context, args=(tJoin,))

tContext.start()
