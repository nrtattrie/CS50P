import pytest
from fuel import convert, gauge


def test_convert():
    with pytest.raises(ValueError):
        convert("A/B")
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    assert convert("1/4") == 25
    assert convert("1/3") == 33
    assert convert("2/3") == 67
    assert convert("3/4") == 75


def test_gauge():
    assert gauge(25) == "25%"
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
