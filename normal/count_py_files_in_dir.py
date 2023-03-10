import os
class Countfiles():
    def __init__(self):
        pass
    def count_files(self,dir):
        self.dir=dir
        self.files=[]
        for file in os.listdir(self.dir):
            p=os.path.splitext(file)
            if p[1]==".py":
                self.files.append(file)
        return self.files
obj=Countfiles()
m=input("enter dir name")
print(obj.count_files(m))
'''instead of using splitext() method we can use "endswith()" method for identifing the file extension'''