from numb3rs import validate

def test_valid():
    assert validate("1.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("127.0.0.1") == True

def test_invalid():
    assert validate("-1.-2.-3.-4") == False
    assert validate("256.256.256.256") == False
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.999") == False
    assert validate("1.2.3.go") == False
    assert validate("cat") == False
    #assert validate("012.111.111.111") == False



