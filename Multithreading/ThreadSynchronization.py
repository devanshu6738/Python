# there is two common thread synchronization mechanism in python
#  1. Lock - Binary nature
#  2. Semaphores - Counting nature    

import time
import threading


# Race condition
a=2

def thread_1():
    global a
    temp=a
    time.sleep(1)
    print("thread 1")
    temp+=a
    a=temp

def thread_2():
    global a
    temp=a
    time.sleep(1)
    print("Thread 2")
    temp+=a
    a=temp

thread__1=threading.Thread(target=thread_1)
thread__2=threading.Thread(target=thread_2)

thread__1.start()
thread__2.start()


print("from main thread")

thread__1.join()
thread__2.join()

print(a)