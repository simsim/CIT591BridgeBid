'''
Bridge Bid
Determine the opening bid of a Contract Bridge game.

@author: xinl, kishin
'''

def highCardPoints(hand):
    faceCardValue = {"A": 4, "K": 3, "Q": 2, "J": 1}
    cardTuple = splitHand(hand)
    sum = 0
    for i in cardTuple:
        sum += faceCardValue.get(i[0], 0)
    return sum

def splitHand(hand):
    handList = hand.split()
    result = []
    for i in handList:
        result.append((i[:-1], i[-1]))
    return tuple(result)
        
def distributionPoints(hand):
    cardTuple = splitHand(hand)
    countPerSuit = {"C": 0, "D": 0, "H": 0, "S": 0}
    sum = 0
    for i in cardTuple:
        countPerSuit[i[-1]] += 1
    for i in countPerSuit.values():
        if i > 4:
            sum += i - 4
    return sum

def openingBid(hand):
    pass