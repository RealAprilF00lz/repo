from factorial import factorial

def test_factorial():
    assert factorial(1)==1
    assert factorial(2)==2
    assert factorial(3)==6
    assert factorial(4)==24
    assert factorial(5)==120
    assert factorial(6)==720
    assert factorial(11)==39916800

def useless():
    x=1
