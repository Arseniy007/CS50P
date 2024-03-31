from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    new_jar = Jar(10)
    assert new_jar.capacity == 10


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(1)
    assert jar.size == 1
    jar.deposit(9)
    assert jar.size == 10


def test_withdraw():
    jar = Jar()
    jar.deposit(12)
    jar.withdraw(1)
    assert jar.size == 11
    jar.withdraw(7)
    assert jar.size == 4
    jar.withdraw(4)
    assert jar.size == 0