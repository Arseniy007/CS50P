import random


while True:
    try:
        level = int(input('Level: '))
        if level > 0:
            break
    except ValueError:
        pass


right = random.randint(1, level)


while True:
    try:
        guess = int(input('Guess: '))
    except ValueError:
        pass
    else:
        if guess < right:
            print('Too small!')
            continue
        elif guess > right:
            print('Too large!')
            continue
        else:
            print('Just right!')
            break
