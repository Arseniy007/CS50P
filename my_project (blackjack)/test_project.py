from project import check_birthday, permission_to_enter, define_winner


def main():
    test_check_birthday()
    test_permission_to_enter()
    test_define_winner()


def test_check_birthday():
    assert check_birthday('24.04.2000') == True
    assert check_birthday('01.01.2022') == True
    assert check_birthday('31.12.1900') == True
    assert check_birthday('16.10.2040') == False
    assert check_birthday('2000.24.04') == False
    assert check_birthday('2000.04.24') == False
    assert check_birthday('16/10/1999') == False
    assert check_birthday('345.2.1987') == False
    assert check_birthday('24042000') == False
    assert check_birthday('cat') == False


def test_permission_to_enter():
    assert permission_to_enter('24.04.2000') == True
    assert permission_to_enter('01.01.1900') == True
    assert permission_to_enter('31.12.2004') == True
    assert permission_to_enter('23.11.1988') == True
    assert permission_to_enter('23.02.2005') == True
    assert permission_to_enter('04.04.2022') == False
    assert permission_to_enter('13.12.2012') == False
    assert permission_to_enter('31.09.2005') == False
    assert permission_to_enter('28.02.2005') == False
    assert permission_to_enter('25.02.2005') == False


def test_define_winner():
    assert define_winner(5, 6) == 'Congratulations! You won this time!'
    assert define_winner(22, 21) == 'Congratulations! You won this time!'
    assert define_winner(100, 15) == 'Congratulations! You won this time!'
    assert define_winner(21, 21) == 'Wow! It looks like a draw'
    assert define_winner(16, 16) == 'Wow! It looks like a draw'
    assert define_winner(10, 7) == 'You lost!'
    assert define_winner(21, 20) == 'You lost!'


if __name__ == '__main__':
    main()
