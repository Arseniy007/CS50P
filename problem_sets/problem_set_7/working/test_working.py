from working import convert
import pytest


def test_pattern():
    assert convert('9 AM to 5 PM') == '09:00 to 17:00'
    assert convert('10:00 AM to 6:00 PM') == '10:00 to 18:00'
    assert convert('10:30 PM to 8:50 AM') == '22:30 to 08:50'
    assert convert('10:30 PM to 8:50 AM') == '22:30 to 08:50'
    assert convert('10:30 PM to 8:50 AM') == '22:30 to 08:50'


def test_value_error_pattern():
    with pytest.raises(ValueError):
        convert('10:00 AM  to  6:00 PM')
    with pytest.raises(ValueError):
        convert('1000 LM to 6:00 PM')
    with pytest.raises(ValueError):
        convert('10 AM to PM')
    with pytest.raises(ValueError):
        convert('10 AM 6 PM')


def test_value_error_digits():
    with pytest.raises(ValueError):
        convert('13 AM to 25 PM')
    with pytest.raises(ValueError):
        convert('10:60 AM to 6:67 PM')
    with pytest.raises(ValueError):
        convert('27:94 AM to 12:800 PM')
