import sys
from blackjack import Blackjack
from datetime import date
from termcolor import colored


def main():
    if start_and_greet() == 'start':
        print('', colored('I need to check your age first.\nWrite your birthday in DD.MM.YYYY format:', 'yellow'), sep='\n\n')
        while True:
            birthday = input()
            if check_birthday(birthday):
                break
            else:
                print('Invalid date')
                continue
        if permission_to_enter(birthday):
            print(colored('Welcome to the game!', 'green', 'on_blue'))
            play()
        else:
            sys.exit('Permission denied')
    else:
        sys.exit('See you next time! :)')


def play():
    game = Blackjack()
    game.deal()
    secret_card, my_card = game.my_cards()[0], game.my_cards()[1]
    my_hand = f'My hand: 🂠 {my_card}'
    print('', my_hand, game, sep='\n')
    while True:
        print()
        answer = get_answer()
        if answer == 'reveal':
            break
        else:
            game.add_card()
            print('', my_hand, game, sep='\n')
            if game.counting_cards()[1] <= 21:
                continue
            else:
                print(colored('Sorry! But that was fun', 'green', 'on_red'))
                another_game()
    result = define_winner(game.counting_cards()[0], game.counting_cards()[1])
    print('', f'My hand: {secret_card} {my_card}', game, sep='\n')
    print(colored(result, 'green', 'on_red'))
    another_game()


def check_birthday(birthday):
    try:
        day, month, year = birthday.split('.')
        if year[0:2] in ['19', '20'] and int(year) < int(date.today().year) and 1 <= int(month) <= 12 and 1 <= int(day) <= 31:
            return True
        else:
            return False
    except ValueError:
        return False


def permission_to_enter(birthday):
    current_year = int(date.today().year)
    users_birthday, users_birthmonth, users_birthyear = birthday.split('.')
    users_age = current_year - int(users_birthyear)
    if users_age > 18:
        return True
    elif users_age == 18:
        current_month = int(date.today().month)
        if int(users_birthmonth) < current_month:
            return True
        elif int(users_birthmonth) == current_month:
            current_day = int(date.today().day)
            if int(users_birthday) < current_day:
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def start_and_greet():
    print('', colored('Hi! Shall we play Blackjack?', 'yellow'), '', sep='\n')
    print()
    while True:
        answer = input("Write 'start' / 'exit':  ")
        if answer in ['start', 'exit']:
            return answer
        else:
            continue


def get_answer():
    while True:
        answer = input("Write 'reveal' to reveal cards, 'add' to add one more: ")
        if answer in ['reveal', 'add']:
            return answer
        else:
            continue


def define_winner(my_total, users_total):
    if my_total > 21 or my_total < users_total:
        return 'Congratulations! You won this time!'
    elif my_total == users_total:
        return 'Wow! It looks like a draw'
    else:
        return 'You lost!'


def another_game():
    print('Do you want to play again?')
    while True:
        answer = input("'yes' / 'no':  ")
        if answer in ['yes', 'no']:
            break
        else:
            continue
    if answer == 'yes':
        play()
    else:
        sys.exit('See you next time! :)')


if __name__ == '__main__':
    main()
