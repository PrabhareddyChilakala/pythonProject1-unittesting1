import threading
import time
def demo1(n):
    for i in range(n):
        time.sleep(0.1)
        print(i,end='\t')
def demo2(n):
    for i in range(n):
        time.sleep(0.1)
        print(i,end='\t')
t1=threading.Thread(target=demo1,args=[1000])
t2=threading.Thread(target=demo2,args=[10])
t1.start()
t1.join()
t2.start()
# output for without giving join:0	0	1	1	2	2	3	3	44		5	5	6	6	7	7	8	8	9	9
# output when join is given: 0	1	2	3	4	5	6	7	8	9	0	1	2	3	4	5	6	7	8	9