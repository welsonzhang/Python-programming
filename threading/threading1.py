# encoding: UTF-8
import threading

def func():
    print 'func() passed to Thread'

t = threading.Thread(target=func)
t.start()

class MyThread(threading.Thread):
    def run(self):
        print "myThread extended from Thread"

t = MyThread()
t.start()
