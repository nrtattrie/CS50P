from bank import value

def test_0():
    assert value("hello") == 0
    assert value("  hello    ") == 0
    assert value("Hello") == 0
    assert value("HELLO") == 0
    assert value("hello, Newman") == 0


def test_20():
    assert value("h") == 20
    assert value("hey") == 20


def test_100():
    assert value("sup") == 100
    assert value("oh hey") == 100
    assert value("What's happening?") == 100
