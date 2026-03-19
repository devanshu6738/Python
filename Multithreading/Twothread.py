import time
import threading

def Thread_1():
    for i in range(5):
        time.sleep(1)
        print("thread 1 : {}".format(i))

def Thread_2():
    for i in range(5):
        time.sleep(1)
        print("thread 2 : {}".format(i))


Thread__1=threading.Thread(target=Thread_1)
Thread__2=threading.Thread(target=Thread_2)

Thread__1.start()
Thread__2.start()

print("from main thread")


Thread__1.join()
Thread__2.join()




