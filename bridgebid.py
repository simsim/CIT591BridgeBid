'''
Bridge Bid
Determine the opening bid of a Contract Bridge game.

@author: xinl@seas.upenn.edu, kishin@seas.upenn.edu
'''

faceCardValue = {"A" : 4, "K" : 3, "Q" : 2, "J" : 1}

def highCardPoints(hand):
    cardTuple = separateHand(hand)
    sum = 0
    for i in cardTuple:
        sum += faceCardValue.get(i[0], 0)
    return sum

def separateHand(hand):
    listHand = hand.split()
    result = []
    for i in listHand:
        result.append((i[:-1], i[-1]))
    return tuple(result)
        
def distributionPoints(hand):
    cardTuple = separateHand(hand)
    #clubs = diamonds = hearts = spades = -4
    count = {"C": -4, "D": -4, "H": -4, "S": -4}
    sum = 0
    for i in cardTuple:
        count[i[-1]] += 1
    for i in count.values():
        if i > 0: sum += i 
    return sum