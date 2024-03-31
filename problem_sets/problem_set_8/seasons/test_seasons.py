from seasons import convert_to_the_right_format


def test_convert_to_the_right_format():
    assert convert_to_the_right_format(525600) == 'Five hundred twenty-five thousand, six hundred minutes'
