name = input('What is your name: ')

for letter in name:
    if letter.isupper():
        print('_' + letter.lower(), end='')
    else:
         print(letter, end='')
