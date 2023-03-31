import threading
class Cls_square(threading.Thread):
    def __init__(self,number):
        threading.Thread.__init__(self)
        self.num=number
    def cal(self):
        for i in range(self.num):
            print(i*i)
    def run(self):
        self.cal()
t1=Cls_square(100)
t1.start()
