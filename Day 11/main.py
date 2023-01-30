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
isRunning = True
player1 = []
player2 = []
wins, losses = 0, 0


def roundEnd():
    global isRunning, player1, player2
    if (input("Do you want to play again? (y/n) ") == "n"):
        isRunning = False
    else:
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


while (isRunning):
    # if(player1[])
    player1.append(cards.pop())
    player2.append(cards.pop())

    print(getSum(player1))
    print(player2)

    roundEnd()
