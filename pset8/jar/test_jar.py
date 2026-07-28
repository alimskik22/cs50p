import pytest
from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0


def test_str():
    jar = Jar()
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"


def test_deposit():
    jar = Jar(5)
    jar.deposit(5)
    assert jar.size == 5


def test_withdraw():
    jar = Jar(5)
    jar.deposit(5)
    jar.withdraw(2)
    assert jar.size == 3



def test_neg_capacity():
    with pytest.raises(ValueError):
        Jar(-1)
