import threading
import time
count=0
def increament():
    global count
    for i in range(100):
        # time.sleep(1)
        count+=1
t1=threading.Thread(target=increament)
t2=threading.Thread(target=increament)
t3=threading.Thread(target=increament)
t4=threading.Thread(target=increament)


t1.start()
t2.start()
t3.start()
t4.start()
# t1.join()
# t2.join()
print("Count is:",count)