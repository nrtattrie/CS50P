from plates import is_valid


def test_basics():
    assert is_valid("CS50") == True


def test_length():
    assert is_valid("") == False
    assert is_valid("a") == False
    assert is_valid("aa") == True
    assert is_valid("aaaaaa") == True
    assert is_valid("aaaaaaa") == False
    assert is_valid("OUTATIME") == False


def test_two_alpas():
    assert is_valid("a123") == False
    assert is_valid("1abc") == False
    assert is_valid("12ab") == False
    assert is_valid("ab12") == True


def test_alphanumeric():
    assert is_valid("ab12!") == False
    assert is_valid("ab.12") == False
    assert is_valid("ab1.2") == False
    assert is_valid("ab12 ") == False
    assert is_valid("ab1 2") == False
    assert is_valid("PI3.14") == False


def test_first_num_zero():
    assert is_valid("ab01") == False
    assert is_valid("ab10") == True
    assert is_valid("CS05") == False


def test_middle_nums():
    assert is_valid("ab12c") == False
    assert is_valid("ab01") == False
    assert is_valid("CS50P") == False


