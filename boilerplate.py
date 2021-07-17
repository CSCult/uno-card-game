"""
@Author: ADD YOUR NAME HERE
@Date Created: ADD DATE CREATED
@Title: UNO CARD GAME

"""

# Importing libraries
import random

'''
Generate the UNO deck of 108 cards.
Parameter: None
Return value: deck->list 
'''


def buildDeck():
    deck = []
    colors = []
    values = []
    wilds = []

    # appending combination of all this 3 list into the deck using for loops
    # formate for this -> (color,values)

    return deck


"""
Shuffles a list of item passed into item
Parameters: deck->list
Return value: deck->list
"""


def shuffleDeck(deck):
    # using for loop in the range of len(deck)
    # generating random number from 0 to 107 as position for cards using the random library

    randPos = random.randint(star, end-1)
    # swapping values (cardPos and cardVal)

    return deck


"""
Draw card function that draws a specified number of cards off the top of the deck.
Parameters: numCards-> integer
Return: cardDrawn -> list
"""

unoDeck = buildDeck()  # storing the cards in a variable
unoDeck = shuffleDeck(unoDeck)  # storing shuffled deck in a variable
discards = [] # list for our discard pile


def drawCards(numCards):
    cardDrawn = []
    #  using for loop in range of numCards (number of cards required to be drawn)
    for _ in range(numCards):
        # using pop as it removes the value from the list(unoDeck) so we don't have to worry about that and appending cards in cardDrawn
    return cardDrawn

"""
Print formatted list of player's hand
Parameter: player->integre, playerHand = List
Return: none....we will be printing the cards
    here we have 0 based indexing so we have to use +1 while printing as we want our cards to start from 1 not 0 keep that in mind
"""
def showHand(player, playerHand):
    # printing whose turn it is with +1 for index
    print("Your Hand")
    print("*****************************")
    x = 1 # index for the cards
    for card in playerHand:
        # printing cards in the formate of (x,card)
        x+=1 # incrementing x
    print("")

"""
Check whether a player is able to play a card or not
Parameters: color->string, value->string, playerHand-> list
If the card is a Wild, they can play no matter what
"""

def canPlay(color, value, playerHand):
    # checking cards in playerHand returning true if color or value is present or the card is wild else returning false
    for card in playerHand:
        #your code
    return False

players = []
colors = ["Red", "Green", "Yellow", "Blue"]

# taking number of players as input we will be having 2 to 4 players
numPlayers = int(input("Enter the number of players: "))

# now you have to check whether the user has entered currect number of player

# now we will draw 5 cards for each player using a for loop and append those cards into the player list(line 65)

# making a variable to keep track of player turn and which direction we are playing

playerTurn = 0
playDirection = 1
playing = True
discards.append(unoDeck.pop(0))# appending top card from unodeck to our discard pile

'''
Preparing card and value for canPlay function
We will create variables for current color and current value we will use [.split] method to get these 2 values
we will store the result from [.split] in a list which will be in the format [color,value]
then we will assign respective values to the variables
'''

"""
***The main playing function***

In this part we will use canPlay function to check whether a player can play or not,
then we will check according to their cards for example, player 1 have a wild card so he can play no matter what, like this we will have conditions for all the special cards.
Here we will also check if the player has won or not.

Now after this canPlay we will increase the playerTurn and change the direction if necessary.
"""

#printing the winner