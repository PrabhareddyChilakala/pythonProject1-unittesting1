def Factorial(self,n):
    self.num=n
    self.fact=1
    while(self.num>0):
        fact=fact*(n)
        n-=1
    return fact
