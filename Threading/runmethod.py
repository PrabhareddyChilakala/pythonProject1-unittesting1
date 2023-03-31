import threading
class Mythread(threading.Thread):
    def __init__(self,thread_name,thread_ID):
        threading.Thread.__init__(self)
        self.thread_name=thread_name
        self.thread_ID=thread_ID
    def run(self):
        print("Thread name"+str(self.thread_name)+" "+"thread_id"+str(self.thread_ID))
        print("Hello from run method")
t1=Mythread("thread1",2)
t2=Mythread("thread2",3)
t1.start()
t2.start()
