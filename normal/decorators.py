def fun1(fun2):
    def wrapper(sal):
        print("fun1:",sal+200)
        fun2(sal)
    return wrapper
def fun2(n):
    print(n)
fun2 fun1(fun2)
fun2(10)
