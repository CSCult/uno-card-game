
#Author: Sujal Samai
#Date Created: 1 Aug,2021
#Title: UNO CARD GAME



# Importing libraries
import random

'''
Generate the UNO deck of 108 cards.
Parameter: None
Return value: deck->list 
'''


def buildDeck():
    deck = []
    colors = ["Red","Green","Yellow","Blue"]
    values = [0,1,2,3,4,5,6,7,8,9,"Draw Two","Skip","Reverse"]

    # appending combination of all this 3 list into the deck using for loops
    for color in colors:
        for value in values:
            card="{} {}".format(color, value)              # formate for this -> (color,values)
            deck.append(card)
            if value !=0:
                deck.append(card)
    
    wilds = ["Wild","Wild draw four"]
    for wild in range(4):
        deck.append(wilds[0])
        deck.append(wilds[1])
    
    #print(deck)
    return deck

uno_deck= buildDeck()