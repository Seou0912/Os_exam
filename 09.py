import threading, os


def func():
    print(" Hi! It's a test function")
    print(" My process Id :", os.getpid())
    print(" Thread Process Id :", threading.get_native_id())


if __name__ == "__main__":
    print(" source process Id :", os.getppid())
    thread1 = threading.Thread(target=func)
    thread1.start()
