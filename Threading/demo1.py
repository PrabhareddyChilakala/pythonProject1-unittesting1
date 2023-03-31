import threading
def mythread():
    print("start thread")
    print("hello")
    print(threading.currentThread().getName())
    print("finished thread")
t1=threading.Thread(target=mythread)
print(threading.currentThread().getName())
t1.start()