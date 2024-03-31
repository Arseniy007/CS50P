from random import shuffle, choice


class Blackjack():
    def __init__(self):
        self._deck = ['2♠', '2♣', '2♦', '2♥', '3♠', '3♣', '3♦', '3♥', '4♠', '4♣', '4♦', '4♥', '5♠',
                    '5♣', '5♦', '5♥', '6♠', '6♣', '6♦', '6♥', '7♠', '7♣', '7♦', '7♥', '8♠', '8♣',
                    '8♦', '8♥', '9♠', '9♣', '9♦', '9♥', '10♠', '10♣', '10♦', '10♥', 'Jack♠', 'Jack♣',
                    'Jack♦', 'Jack♥', 'Queen♠', 'Queen♣', 'Queen♦', 'Queen♥', 'King♠', 'King♣',
                    'King♦', 'King♥', 'Ace♠', 'Ace♣', 'Ace♦', 'Ace♥']
        self._users_cards = []
        self._my_cards = []


    def __str__(self):
        output = 'Your hand:'
        for card in self._users_cards:
            output += f' {card}'
        return output


    @property
    def deck(self):
        return self._deck


    @property
    def users_cards(self):
        return self._users_cards


    @property
    def my_cards(self):
        return self._my_cards


    def my_cards(self):
        return self._my_cards


    def deal(self):
        shuffle(self._deck)
        number_of_cards = 4
        for i in range(number_of_cards):
            card = choice(self._deck)
            self._deck.remove(card)
            if i % 2 == 0:
                self._users_cards.append(card)
            else:
                self._my_cards.append(card)


    def add_card(self):
        new_card = choice(self._deck)
        self._deck.remove(new_card)
        self._users_cards.append(new_card)


    def counting_cards(self):
        card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
                    '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
        my_total, users_total = 0, 0
        for card in self._my_cards:
            card = card[:-1]
            my_total += card_values[card]
        for card in self._users_cards:
            card = card[:-1]
            users_total += card_values[card]
        return [my_total, users_total]
