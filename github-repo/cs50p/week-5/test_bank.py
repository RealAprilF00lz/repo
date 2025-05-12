from bank import value

def test_hello():
    assert value('Hello, world')==0

def test_h():
    assert value('hi FRIEND!')==20

def test_other():
    assert value('whats up, bro')==100
