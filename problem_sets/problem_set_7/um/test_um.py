from um import count


def test_words_with_um():
    assert count('cryptosporidium') == 0
    assert count('um, cryptosporidium, um, umbrella') == 2
    assert count('umumum') == 0
    assert count('overdocumenting ist, um, something') == 1


def test_the_cases():
    assert count('UM, uM, Um, um') == 4
    assert count('Um, UMBRELLA, UM, mum, uM') == 3


def test_someting():
    assert count('Um') == 1
    assert count('!um') == 1
