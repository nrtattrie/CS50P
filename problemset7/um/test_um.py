import pytest
from um import count

def test_valid():
    assert count("") == 0
    assert count("hello, world") == 0
    assert count("um") == 1
    assert count("um?") == 1
    assert count("...um") == 1
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2
    assert count("Um, hello, um, world") == 2

def test_invalid():
    assert count("yummy") == 0
    assert count("album") == 0
    assert count("uuuummmm") == 0
