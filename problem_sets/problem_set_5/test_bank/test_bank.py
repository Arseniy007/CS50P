from bank import value


def test_value_hello():
    assert value('hello') == 0


def test_value_h():
    assert value('hallo') == 20
    assert value('HAKUNA MATATA') == 20
    assert value('h') == 20


def test_value_100():
    assert value('123') == 100
    assert value("What's up") == 100
    assert value(',.>') == 100