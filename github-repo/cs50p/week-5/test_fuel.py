from fuel import convert,gauge
from pytest import raises

def test_convert():
    assert convert('2/5')==40
    assert convert('1/4')==25
    assert convert('2.1/5')==42
    with raises(ValueError):
        convert('hello')
    with raises(ValueError):
        convert('5/4')
    with raises(ZeroDivisionError):
        convert('5/0')

def test_gauge():
    assert gauge(99)=='F'
    assert gauge(1)=='E'
    assert gauge(42)=='42%'
