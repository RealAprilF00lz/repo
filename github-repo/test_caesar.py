from caesar import caesar
from pytest import raises

def test_caesar():
    with raises(TypeError):
        caesar(5)
    assert caesar('hello, CS50 zZ',7)=='olssv, JZ50 gG'
    assert caesar('hello, CS50 zZ')=='ifmmp, DT50 aA'
    assert caesar('zeBRA!',30)=='diFVE!'
    assert caesar('Hello, world',26)=='Hello, world'
    assert caesar('i like trains?',105)=='j mjlf usbjot?'
    assert caesar('hello, CS50 zZ',555378)=='zwddg, UK50 rR'
