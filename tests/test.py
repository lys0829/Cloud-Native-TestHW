import pytest
from price import price

def testBasics():
    assert 0.0 == price([])
    assert 8.0 == price([1])
    assert 8.0 == price([2])
    assert 8.0 == price([3])
    assert 8.0 == price([4])
    assert 8.0*3.0 == price([1,1,1])

def testSimpleDiscounts():
    assert 8 * 2 * 0.95 == price([0, 1])
    assert 8 * 3 * 0.9 == price([0, 2, 4])
    assert 8 * 4 * 0.8 == price([0, 1, 2, 4])
    assert 8 * 5 * 0.75 == price([0, 1, 2, 3, 4])

def testSeveralDiscounts():
    assert 8 + (8 * 2 * 0.95) == price([0, 0, 1])
    assert 2 * (8 * 2 * 0.95) == price([0, 0, 1, 1])
    assert (8 * 4 * 0.8) + (8 * 2 * 0.95) == price([0, 0, 1, 2, 2, 3])
    assert 8 + (8 * 5 * 0.75) == price([0, 1, 1, 2, 3, 4])

def testEdgeCases():
    assert 2 * (8 * 4 * 0.8) == price([0, 0, 1, 1, 2, 2, 3, 4])
    assert 3 * (8 * 5 * 0.75) + 2 * (8 * 4 * 0.8) == price([0, 0, 0, 0, 0, 
                                                            1, 1, 1, 1, 1, 
                                                            2, 2, 2, 2, 
                                                            3, 3, 3, 3, 3, 
                                                            4, 4, 4, 4])