import random

suits = ['♥', '♦️', '♠️', '♣️']
cards = []

for suit in suits:
    for value in range(1, 14):
        card = {}
        card['suit'] = suit
        card['value'] = value
        if (card['value'] == 1):
            card['symbol'] = 'A'
        elif card['value'] == 11:
            card['symbol'] = 'J'
        elif card['value'] == 12:
            card['symbol'] = 'Q'
        elif card['value'] == 13:
            card['symbol'] = 'K'
        else:
            card['symbol'] = str(card['value'])
        cards.append(card)

random.shuffle(cards)
isRunning, roundOver = True, False
player1 = []
player2 = []
wins, losses = 0, 0

def printHand(player):
    hand = ""
    for x in player:
        hand += f"[{x['value']['suit']}] "
    return hand

def roundEnd():
    global isRunning, roundOver, player1, player2
    if (input("Do you want to play again? (y/n) ") == "n"):
        isRunning = False
    else:
        roundOver = False
        for x in player1:
            cards.append(x)
        for x in player2:
            cards.append(x)
        player1 = []
        player2 = []
        random.shuffle(cards)


def getSum(player):
    sum = 0
    for card in player:
        sum += card['value']
    return sum

def drawCard(player):
    global cards
    player.append(cards.pop())

while (isRunning):
    hitOrPass = ''
    if(getSum(Player1) > 21):
        print("Bust")
        roundOver = True
    else:
        print(f"Your Hand: {printHand(player1)})"
        while hitOrPass not 'h' or hitOrPass not 'p':
            hitOrPass = input("(H)it or (P)ass").lower()
        if hitOrPass == 'p':
            roundOver = True
        else:
            drawCard(player1)
        
#     player1.append(cards.pop())
#     if(getSum(Player2) < 17):
#         player2.append(cards.pop())    
    if(roundOver):
        roundEnd()
