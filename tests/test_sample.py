import pytest


def test_file_1_method1():
    x = 5
    y = 6
    assert x + 1 == y, "test failed"
    assert x == y, "test failed because x=" +str(x) +"y=" + str(y)


def test_file_1_method2():
    x = 5
    y = 6
    assert x+1 == y, "test failed"


