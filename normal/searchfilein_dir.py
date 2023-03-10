import os
class Searchfiles():
    def __init__(self):
        pass
    def search(self,dir,filename):
        self.dir=dir
        self.filename=filename
        self.f=[]
        for root,dir,file in os.walk(self.dir):
            if self.filename in file:
                self.f.append(os.path.join(root,filename))
        return self.f


