from fuel import convert, gauge
import pytest


def test_convert():
    assert convert('1/4') == 25
    assert convert('4/4') == 100


def test_gauge():
    assert gauge(100) == 'F'
    assert gauge(99) == 'F'
    assert gauge(0) == 'E'
    assert gauge(1) == 'E'
    assert gauge(40) == '40%'
    assert gauge(70) == '70%'


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert('1/0')


def test_value_error():
    with pytest.raises(ValueError):
        convert('5/2')


def test_value_2():
    with pytest.raises(ValueError):
        convert('cat/dog')
