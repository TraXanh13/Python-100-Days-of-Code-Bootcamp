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
wins, losses, ties = 0, 0, 0


def printHand(player):
    hand = ""
    for x in player:
        hand += f"[{str(x['symbol'])}{x['suit']}] "
    return hand


def checkWinCon(p1Sum, p2Sum):
    global wins, losses, ties
    if (p1Sum == p2Sum):
        print("Tie")
        ties += 1
    elif (p1Sum > 21 and p2Sum > 21):
        if (p1Sum > p2Sum):
            print("You lost")
            losses += 1
        else:
            print("You won")
            wins += 1
    elif (p1Sum > 21):
        print("You lost")
        losses += 1
    elif (p2Sum > 21):
        print("You won")
        wins += 1
    elif (p1Sum > p2Sum):
        print("You won")
        wins += 1
    else:
        print("You lost")
        losses += 1


def roundEnd():
    global player1, player2
    p1Sum = getSum(player1)
    p2Sum = getSum(player2)

    checkWinCon(p1Sum, p2Sum)

    print(f"Your Hand: {printHand(player1)} --> {p1Sum}")
    print(f"Dealer Hand: {printHand(player2)} --> {p2Sum}")

    replay()


def replay():
    global isRunning, roundOver, player1, player2
    if (input("Do you want to play again? (y/n) ") == "n"):
        isRunning = False
        print(f"Wins: {wins} Losses: {losses} Ties: {ties}")
    else:
        roundOver = False
        for x in player1:
            cards.append(x)
        for x in player2:
            cards.append(x)
        player1 = []
        player2 = []
        print("Shuffling cards...")
        random.shuffle(cards)
        player1.append(cards.pop())
        player2.append(cards.pop())


def getSum(player):
    sum = 0
    for card in player:
        sum += card['value']
    if (sum < 12 and any(card['value'] == 1 for card in player)):
        sum += 10
    return sum


def drawCard(player):
    global cards
    player.append(cards.pop())


drawCard(player1)
drawCard(player2)

while (isRunning):
    hitOrPass = ''
    if (getSum(player1) > 21):
        print("Bust")
        roundOver = True
    else:
        print(f"Your Hand: {printHand(player1)} --> {getSum(player1)}")
        while hitOrPass != 'h' and hitOrPass != 'p':
            hitOrPass = input("(H)it or (P)ass ").lower()
        if hitOrPass == 'p':
            roundOver = True
        else:
            print(f"You drew a {cards[-1]['symbol']}{cards[-1]['suit']}")
            drawCard(player1)

    if (getSum(player2) < 17):
        drawCard(player2)

    if (roundOver):
        roundEnd()
