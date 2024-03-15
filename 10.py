import threading, os, time


def something(word):
    while True:
        print(word)
        time.sleep(3)


if __name__ == "__main__":
    print("source process Id :", os.getpid())
    t = threading.Thread(target=something, args=("happy",))
    t.daemon = True
    t.start()
    print(" Start loop in main thread ")
    while True:
        try:
            print(" daily...")
            time.sleep(1)
        except KeyboardInterrupt:
            print(" Goodbye~~ ")
            break
