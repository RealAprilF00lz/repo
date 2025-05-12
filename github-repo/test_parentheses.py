from parentheses import check
from pytest import raises

def test_parentheses():
    assert check('()')==True
    assert check('print(input())')==True
    assert check(')(')==False
    assert check('(()')==False
    assert check('print())')==False
    assert check('())(')==False
    assert check('(')==False
    assert check(' (foo) (bar) ')==True
    assert check('(()()))(')==False

