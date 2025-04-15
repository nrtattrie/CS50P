from twttr import shorten


def test_vowels():
    assert shorten("twitter") == "twttr"
    assert shorten("sepia") == "sp"
    assert shorten("adieu") == "d"
    assert shorten("mound") == "mnd"
    assert shorten("AEIOU") == ""


def test_phrases():
    assert shorten("What's your name?") == "Wht's yr nm?"
    assert shorten("CS50") == "CS50"
    


