import random

# for reference: https://www.unovariations.com/official-uno-rules

"""
Creates the UNO deck
Return value: Deck -> list
"""


def buildDeck():
    deck = []
    colors = ["Red", "Green", "Yellow", "Blue"]
    values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "Draw Two", "Skip", "Reverse"]
    wilds = ["Wild", "Wild Draw four"]
    # Generating deck
    for color in colors:
        for value in values:
            cardVal = "{} {}".format(color, value)
            deck.append(cardVal)
            if value != 0:
                deck.append(cardVal)
    for i in range(4):
        deck.append(wilds[0])
        deck.append(wilds[1])
    return deck

""" 
Shuffles the deck we just created with
Return value: Deck-> list.
"""
def shuffleDeck(deck):
    for cardPos in range(len(deck)):
        # generating random number from 0 to 107 as position for cards
        randPos = random.randint(0, 107)
        # swapping values
        deck[cardPos], deck[randPos] = deck[randPos], deck[cardPos]
    return deck

"""
Draws specified number of cards from the deck
Return values: cardDrawn-> list
"""
def drawCards(numCards):
    cardDrawn = []
    for x in range(numCards):
        # using pop as it removes the value from the list so we don't have to worry about that
        cardDrawn.append(unoDeck.pop(0))
    return cardDrawn

'''
List of card player have to
pleyer = integer, playerHand = list
Return: None
'''

def showHand(player, playerHand):
    print("Player {}'s turn".format(player+1))  # +1 cause we have index 0
    print("Your Hand")
    print("*****************************")
    x = 1
    for card in playerHand:
        print("{}) {}".format(x,card))
        x+=1
    print("")


'''
Checks whether a player can play or not 
here if discard is Wild they can play no matter what
'''

def canPlay(color, value, playerHand):
    # splitCard = card.split(' ',1) # splits the color and number
        # directly checking ibsted of suing split
    for card in playerHand:
        if "Wild" in card:
            return True
        elif color in card or value in card:
            return True
    return False

unoDeck = buildDeck()
unoDeck = shuffleDeck(unoDeck)  # using shuffle function to shuffle the deck
discards = []
# print(unoDeck)

players = []
colors = ["Red", "Green", "Yellow", "Blue"]

numPlayers = int(input("Enter the number of players: "))
while numPlayers < 2 or numPlayers > 4:
    numPlayers = int(input("Invalid. Please Enter a number between 2-4: "))
for player in range(numPlayers):
    players.append(drawCards(5))

# print(players)
playerTurn = 0
playDirection = 1
playing = True
discards.append(unoDeck.pop(0))

'''
Preparing card and avlue for canPlay function
'''
splitCard = discards[0].split(" ", 1)
currColor = splitCard[0]
if currColor != "Wild":
    cardVal = splitCard[1]
else:
    cardVal = "Any"

while playing:
    showHand(playerTurn, players[playerTurn])
    print("Card on top of discard pile is: {}".format(discards[-1]))
    if canPlay(currColor, cardVal, players[playerTurn]):
        cardChosen =int(input("Which card do you wanna play? "))
        while not canPlay(currColor, cardVal, [players[playerTurn][cardChosen-1]]):
            cardChosen =int(input("Not a valid car. Which card do you wanna play? "))
        print("You played {}".format([players[playerTurn][cardChosen-1]]))
        discards.append(players[playerTurn].pop(cardChosen-1))

        #check if player won
        if len(players[playerTurn])==0:
            playing = False
            winner = "Player {}".format(playerTurn+1)
        else:
            #check for special cards -_- we want the last card
            splitCard = discards[-1].split(" ", 1)
            currColor = splitCard[0]
            if len(splitCard) == 1:
                cardVal = "Any"    # if its a wild card
            else:
                cardVal = splitCard[1]
            if currColor == "Wild":
                for x in range(len(colors)):
                    print("{}) {}".format(x+1,colors[x]))
                newColor = int(input("What color would you like to choose"))
                while newColor<1 or newColor > 4:
                    newColor = int(input("Invalid color. What color would you like to"))
                currColor = colors[newColor-1]

            if cardVal == "Reverse":
                playDirection = playDirection * -1

            elif cardVal == "Skip":
                playerTurn+= playDirection
                if playerTurn >= numPlayers:
                    playerTurn = 0
                elif playerTurn < 0:
                    playerTurn = numPlayers-1
                

            elif cardVal == "Draw Two":
                playerDraw = playerTurn + playDirection
                if playerTurn >= numPlayers:
                    playerTurn = 0
                elif playerTurn < 0:
                    playerTurn = numPlayers-1
                players[playerTurn].extend(drawCards(2))

            elif cardVal == "Draw Four":
                playerDraw = playerTurn + playDirection
                if playerTurn >= numPlayers:
                    playerTurn = 0
                elif playerTurn < 0:
                    playerTurn = numPlayers-1
                players[playerTurn].extend(drawCards(4))

            print("")
    else:
        print("You cant play. You have to draw a card.")
        players[playerTurn].extend(drawCards(1))
    print("")

    playerTurn += playDirection
    if playerTurn >= numPlayers:
        playerTurn = 0
    elif playerTurn < 0:
        playerTurn = numPlayers-1

'''
Here in no canPlay we used multiple [] cause we want a list as the third parameter for us it will return string so we have used [] to make it list... in the pop part we used -1 cause we have 0 based indexing..... and we used extend cause we just want to concatinate(merge) two list by using append it would have been more complex
'''

print("Game Over")
print("{} is the winner!".format(winner))