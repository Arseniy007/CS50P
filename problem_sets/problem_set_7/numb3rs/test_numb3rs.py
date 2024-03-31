from numb3rs import validate


def test_the_pattern():
    assert validate('9.100.144.90') == True
    assert validate('100.100.99.0') == True
    assert validate('cat') == False
    assert validate('....') == False
    assert validate('cat.100.dog.99') == False


def test_the_numbers():
    assert validate('0.19.234.255') == True
    assert validate('0.0.0.255') == True
    assert validate('909.100.344.90000') == False
    assert validate('-1.-100.-55.-90') == False
    assert validate('75.456.56.98') == False