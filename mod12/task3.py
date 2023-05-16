from threading import Semaphore, Thread
import time

sem: Semaphore = Semaphore()
stop_flag = False

def fun1():
    global stop_flag
    while not stop_flag:
        sem.acquire()
        print(1)
        sem.release()
        time.sleep(0.25)

def fun2():
    global stop_flag
    while not stop_flag:
        sem.acquire()
        print(2)
        sem.release()
        time.sleep(0.25)

t1: Thread = Thread(target=fun1)
t2: Thread = Thread(target=fun2)

try:
    t1.start()
    t2.start()
    while True:
        time.sleep(0.1)
except KeyboardInterrupt:
    stop_flag = True
    t1.join()
    t2.join()
    print('\nReceived keyboard interrupt, quitting threads.')
    exit(1)
