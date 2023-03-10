import pytest
@pytest.mark.hcl
def test_d1():
    assert 10+4==14
def test_d2():
    assert 11-2==9
@pytest.mark.hcl
def test_d3():
    assert 11*2==22
def test_d4():
    assert 10/2==5