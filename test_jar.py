from jar import Jar
import pytest


def test_init():
    jar = Jar()
    assert jar.capacity == 12

    jar = Jar(20)
    assert jar.capacity == 20

    with pytest.raises(ValueError):
        Jar(-1)


def test_str():
    jar = Jar()

    assert str(jar) == ""

    jar.deposit(1)
    assert str(jar) == "🍪"

    jar.deposit(2)
    assert str(jar) == "🍪🍪🍪"


def test_deposit():
    jar = Jar(5)

    jar.deposit(3)
    assert jar.size == 3

    with pytest.raises(ValueError):
        jar.deposit(3)


def test_withdraw():
    jar = Jar()

    jar.deposit(5)
    jar.withdraw(2)

    assert jar.size == 3

    with pytest.raises(ValueError):
        jar.withdraw(4)
