import pytest
from price import price

def testBasics():
    assert 0.0 == price([])
    assert 8.0 == price([1])
    assert 8.0 == price([2])
    assert 8.0 == price([3])
    assert 8.0 == price([4])
    assert 8.0*3.0 == price([1,1,1])