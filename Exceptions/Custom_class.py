from Exceptions.listnums_exception import Hcl_list_exception
class Mylist():
    def __init__(self):
        self.list=[]
    def insertele(self):
        try:
            n=input("enter the value")
            if not isinstance(n,int):
                raise Hcl_list_exception("invalid input")
            else:
                self.list.append(n)
        except Hcl_list_exception as e:
            print(e)
obj=Mylist()
obj.insertele()