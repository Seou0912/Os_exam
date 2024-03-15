from multiprocessing import Process
import os, time


def coke():
    print("coke process Id: ", os.getpid())
    print("parent process Id: ", os.getpid())


def cider():
    print("cider process Id: ", os.getpid())
    print("parent process Id: ", os.getpid())


def juice():
    print("juice process Id: ", os.getpid())
    print("parent process Id: ", os.getpid())


if __name__ == "__main__":
    print(" 07.py process Id :", os.getppid())
    child1 = Process(target=coke)
    child1.start()
    time.sleep(1)
    child2 = Process(target=cider)
    child2.start()
    time.sleep(1)
    child3 = Process(target=juice)
    child3.start()
    time.sleep(1)
