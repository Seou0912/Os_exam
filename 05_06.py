from multiprocessing import Process
import os, time


def func():
    print(" Hi! It's a test function")
    print(" My process Id :", os.getpid())
    print(" My parent Process Id :", os.getppid())


if __name__ == "__main__":
    print(" 04.py process Id :", os.getppid())
    child1 = Process(target=func)
    child1.start()
    time.sleep(1)
    child2 = Process(target=func)
    child2.start()
    time.sleep(1)
    child3 = Process(target=func)
    child3.start()
    time.sleep(1)
