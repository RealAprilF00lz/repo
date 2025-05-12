from seasons import calculate
from pytest import raises

def test_invalid():
    with raises(ValueError):
        calculate('hello world')
    with raises(ValueError):
        calculate('January 2, 2020')

def test_valid():
    #these tests won't work after the day they were written lmao
    assert calculate('2025-03-10')=='twelve thousand, nine hundred sixty minutes'
    assert calculate('2024-03-19')=='five hundred twenty-five thousand, six hundred minutes'
    assert calculate('2025-03-19')=='zero minutes'
