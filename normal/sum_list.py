import pytest
def list_sum(a):
    sum=0
    for i in a:
        sum+=i
    return sum
@pytest.mark.parametrize("a,expected_output",[([1,2],3),([4.5,5,6],15.5),([4,5,8],17)])
def test_sum(a,expected_output):
    assert list_sum(a)==expected_output
'''instead of using for loop we can directly use sum(a) for printing of sum of numbers in a list'''
