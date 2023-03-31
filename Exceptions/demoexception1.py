from Exceptions.custome_exceptions import Myexception
try:
    age=int(input("enter the age"))
    if age<18:
        raise Myexception("Age is invalid")
    else:
        print(age)
except Myexception as e:
    print(e)