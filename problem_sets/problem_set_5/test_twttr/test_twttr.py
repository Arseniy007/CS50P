from twttr import shorten


def test_shorten():
    assert shorten('Twitter') == 'Twttr'
    assert shorten('GOMARDJOBA') == 'GMRDJB'
    assert shorten('1234') == '1234'
    assert shorten("What's your name?") == "Wht's yr nm?"
