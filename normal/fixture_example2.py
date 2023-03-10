import pytest
@pytest.fixture
def setUp():
    print("Open Browser")
    print("Login")
    print("Browse the product")
'''while calling setUp function in test_add then all first 3 prints will execute first and 
later test_add function will execute and later yeild will runs'''
    yeild
    print("Close the browser")
def test_add(setUp):
    print("Add items to cart")
def test_delete(setUp):
    print("Remove an item from the cart")