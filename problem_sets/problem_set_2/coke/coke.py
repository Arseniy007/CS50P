amount = 50

while amount > 0:
    print('Amount Due:', amount)
    coin = int(input('Insert coin: '))
    if coin == 5 or coin == 10 or coin == 25:
        amount -= coin

change = abs(amount)

print('Change Owed:', change)
