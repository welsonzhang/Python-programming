#!/usr/bin/python
#-*- coding: UTF-8 -*-

import threading
import time

class myThread(threading.Thread):
    def __init__(self,threadID,name,counter):
        threading.Thread.__init__(self)
        self.threadID=threadID
        self.name=name
        self.counter=counter

    def run(self):
        print "Starting "+self.name
        #acquire the lock return ture
        #timeout is None it will block to wait the lock
        #or it will return False when timeout
        threadLock.acquire()
        print_time(self.name,self.counter,3)
        #release the lock
        threadLock.release()
        
def print_time(threadName,delay,counter):
    while counter:
        time.sleep(delay)
        print "%s: %s"%(threadName,time.ctime(time.time()))
        counter-=1

threadLock=threading.Lock()
threads=[]

#create new thread
thread1=myThread(1,"Thread-1",1)
thread2=myThread(2,"Thread-2",2)

#start new thread
thread1.start()
thread2.start()

#add the thread to the thread list
threads.append(thread1)
threads.append(thread2)

#wait all thread complete
for t in threads:
    t.join()
print "Exit Main Thread"
