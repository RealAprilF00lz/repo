from jar import Jar
from pytest import raises


def test_init():
    jar=Jar()
    assert jar.capacity==12
    assert jar.size==0
    jar=Jar(6)
    assert jar.capacity==6
    assert jar.size==0
    jar=Jar(0)
    assert jar.capacity==0
    assert jar.size==0
    with raises(ValueError):
        jar=Jar('hello')
    with raises(ValueError):
        jar=Jar(-1)
    with raises(ValueError):
        jar=Jar(5.4)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar=Jar(5)
    with raises(ValueError):
        jar.deposit(6)
    jar.deposit(4)
    assert jar.size == 4


def test_withdraw():
    jar=Jar()
    jar.deposit(7)
    with raises(ValueError):
        jar.withdraw(8)
    jar.withdraw(5)
    assert jar.size==2

