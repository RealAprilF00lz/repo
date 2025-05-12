from working import convert
from pytest import raises

def test_invalid_input():
    with raises(ValueError):
        convert('cat')
    with raises(ValueError):
        convert('13 AM to 2:60 PM')

def test_no_minutes():
    assert convert('9 AM to 5 PM')=='9:00 to 17:00'
    assert convert('7 PM to 10 AM')=='19:00 to 10:00'

def test_minutes():
    assert convert('9 AM to 5:31 PM')=='9:00 to 17:31'
    assert convert('2:40 PM to 9:00 PM')=='14:40 to 21:00'
