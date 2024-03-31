from plates import is_valid


def test_length():
    assert is_valid('AA') == True
    assert is_valid('ABCD') == True
    assert is_valid('ACDEF') == True
    assert is_valid('ABCDEFGHIJK') == False
    assert is_valid('A') == False


def test_first_two_letters():
    assert is_valid('AABN22') == True
    assert is_valid('BVBf2') == True
    assert is_valid('BV2') == True
    assert is_valid('V1DDD') == False
    assert is_valid('12ABC') == False
    assert is_valid('?AB21') == False
    assert is_valid('A') == False
    assert is_valid('C50') == False



def test_nothing_odd():
    assert is_valid('AVCD23') == True
    assert is_valid('ABC 23') == False
    assert is_valid('32,?BN') == False
    assert is_valid('1B,?BN') == False


def test_no_digits_in_the_middle():
    assert is_valid('AABC21') == True
    assert is_valid('ABCDEF') == True
    assert is_valid('ABCD09') == False
    assert is_valid('AA23BN') == False
