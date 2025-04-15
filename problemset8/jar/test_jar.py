import pytest
from jar import Jar


def test_init():
    jar = Jar()
    assert jar.size == 0
    assert jar.capacity == 12

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    one_jar = "🍪"
    seven_jar = "🍪🍪🍪🍪🍪🍪🍪"
    twelve_jar = "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

    jar = Jar()
    jar.deposit(1)
    assert str(jar) == one_jar
    jar.deposit(6)
    assert str(jar) == seven_jar
    jar.deposit(5)
    assert str(jar) == twelve_jar

    with pytest.raises(ValueError):
        jar.deposit(1)


def test_withdraw():
    jar = Jar()
    jar.deposit(12)
    zero_jar = ""
    one_jar = "🍪"
    seven_jar = "🍪🍪🍪🍪🍪🍪🍪"
    eleven_jar = "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

    jar.withdraw(1)
    assert str(jar) == eleven_jar
    jar.withdraw(4)
    assert str(jar) == seven_jar
    jar.withdraw(6)
    assert str(jar) == one_jar
    jar.withdraw(1)
    assert str(jar) == zero_jar

    with pytest.raises(ValueError):
        jar.withdraw(1)

