import pytest
from seasons import convert

def test_valid():
    assert convert("2025-02-26") == "Zero minutes"
    assert convert("2024-02-26") == "Five hundred twenty-seven thousand forty minutes"
    assert convert("2023-02-26") == "One million, fifty-two thousand, six hundred forty minutes"
    assert convert("2024-02-29") == "Five hundred twenty-two thousand, seven hundred twenty minutes"
    assert convert("1996-02-05") == "Fifteen million, two hundred eighty-four thousand, one hundred sixty minutes"


def test_invalid():
    with pytest.raises(ValueError):
        convert("cat")
    with pytest.raises(ValueError):
        convert("20-01-01")
    with pytest.raises(ValueError):
        convert("20000-01-01")
    with pytest.raises(ValueError):
        convert("2000-01-011")
    with pytest.raises(ValueError):
        convert("2000-13-01")
    with pytest.raises(ValueError):
        convert("2000-01-40")
    with pytest.raises(ValueError):
        convert("2025-02-29")
