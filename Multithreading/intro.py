import threading
import time
from datetime import datetime

def thread_function_1():
    for i in range(5):
        print("Thread 1:{}".format(i))
        time.sleep(2)  #i/o bound
        print(datetime.now())

thread1=threading.Thread(target=thread_function_1)

thread1.start()
print("from main thread")
print(thread1.is_alive())

thread1.join()

# # thread state
print(thread1.is_alive())