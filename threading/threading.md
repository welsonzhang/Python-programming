Threading Method
----------------
## Thread
### Construction Method
Thread(group=None, target=None, name=None, args=(), kwargs={}) 
- group: thread group always None
- target: method to run
- name: thread name
- args/kwargs: the argument of the method

### Instance Method
- isAlive(): return the thread whether alive
- get/setName(name): get or set the name of thread
- start(): run the thread
- join(timeout): wait for the thread, until timeout

## Lock
### Construction Method
- Lock()
### Instance Method
- acquire([timeout]): block, util get the lock
- release(): release the lock. must own the lock before

## RLock
### Construction Method
- RLock()
### Instance Method
- acquire([timeout])/release()

## Condition
### Construction Method
- Condition([lock/rlock])
### Instance Method
- acquire([timeout])/release(): 
- wait([timeout])
- notify()
- notifyAll()

## Semaphore/BoundedSemaphore
### Construction Method
- Semaphore(value=1): value the count 
### Instance Method
- acquire([timeout]):
- release()

## Event
### Construction Method
- Event()
### Instance Method
- isSet():
- set():
- clear():
- wait([timeout]): 

## Timer
### Construction Method
- Timer(interval, function, args=[], kwargs={}) 
- interval
- function
- args/kwargs

## local
