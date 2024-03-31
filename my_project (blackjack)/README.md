# Blackjack
#### Video Demo: https://www.youtube.com/watch?v=LCEx1dd3GTE
#### Description:
Hello everyone! This is 'Blackjack'! A program where you can play Blackjack with a computer (without betting, of course! :) )
The main file ('project.py') contains a 'main' function and seven additional functions. In blackjack.py file locates the class Blackjack, which the program actively uses. test_project.py tests a bunch of functions from the main 'project.py' file. And lastly, we have requirements.txt where all pip-installed libraries are listed (in our case only one - termcolor).

##### project.py:
1) **main** function describes the general design of the program. Using 'start_and_greet' function checks if the user really wants to play blackjack (if not - then the program exits) and then using another two functions checks the user's age. If the user is older than 18 years and wants to play it initiates the 'play' function inside which all the game logic is put;

2) **play** function describes the logic of one turn of the game. Each turn it creates an object 'game' of 'Blackjack' class (implemented in file 'blackjack.py'), deals cards, prints both users and croupier's (computer's) hands, allows the user to add cards using a loop, checks if the user does not have more than 21 points (in this case **play** function tells the user that game is over), lastly using 'define_winner' function it counts both croupier's and user's total point and prints the game result;

3) **check_birthday** function checks if the user has put his birthday in a required format *(DD.MM.YYYY)* and if the given date is valid;

4) **permission_to_enter** function takes the user's birthday (in the right format) as an argument and checks if the user is older than 18 years (using datetime module);

5) **start_and_greet** function does start and does greet a user (also checks if they want to play at all);

6) **get_answer** function is implemented to get an answer from the user. Does he want to reveal the croupier's card, or does he want to add another card to his hand? It does not allow the user to write something besides 'reveal' or 'add' also;

7) **define_winner** function takes to arguments: croupiers and user's total scores and decides who of them won. It returns a str-result, which will be later printed;

8) **another_game** function asks the user if he wants to play one more time. If the answer is 'no' the program exits if 'yes' it calls the 'play' function and the process begins from scratch if the user writes something besides 'yes' or 'no' they would be asked once again.

##### blackjack.py:

Here we have Blackjack class with three properties (full deck of cards, user's hand, and croupier's hand) and three main methods:

1) **deal** method shuffles the deck using the 'random' module and deals four (also random) cards: two to the croupier's, two to the user's hands

2) **ad_card** method takes and removes one random card from the shuffled deck and appends it to the user's hand

3) **counting_cards** method counts the total score for both user's and croupier's hands using the card_values dictionary.

##### test_project.py:
Here we have three testing functions: test_check_birthday, test_permission_to_enter, and test_define_winner