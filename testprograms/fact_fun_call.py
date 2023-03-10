from testprograms import prg_factorial
n=int(input("enter num:"))
if n == 0:
    print(1)
elif n < 0 or not isinstance(n,int):
    print("Only positive numbers are allowed")
else:
    obj=prg_factorial()
    print(obj.Factorial(n))