import pytest
def factors(n):
    l=[]
    for i in range(2,n):
        if n%i==0:
            l.append(i)
    return l
@pytest.mark.parametrize("n,exp_out",[(10,[2,5]),(12,[2,3,4,6])])
def fac(n,exp_out):
    assert factors(n)==exp_out