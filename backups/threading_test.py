import threading
import time
def test1():
    for i in range(10000):
        print("test with threading 1:{0}".format(time.time()))
        time.sleep(0.5)

def test2():
    for i in range(10000):
        print("test with threading 2:{0}".format(time.time()))
        time.sleep(0.5)
threads = []
t1 = threading.Thread(target=test1)
threads.append(t1)
t2 = threading.Thread(target=test2)
threads.append(t2)

if __name__ == "__main__":
    for t in threads:
        t.start()
    for t in threads:
        t.join()
print("exit")