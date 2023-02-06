import art
import random as r
from game_data import data as gd
import time, os

isRunning = True
score = 0
compareA = r.choice(gd)

def printCompare(compare):
    return f'{compare["name"]} a {compare["description"]} from {compare["country"]}'
    
def GameSetUp(compareA, compareB):
    print(art.logo)
    print(f"Compare A: {printCompare(compareA)}\n\n")
    print(art.vs)
    print(f"\n\nCompare B: {printCompare(compareB)}\n\n")


def checkGuess(compareB, guess):
    global compareA, score
    if (guess == 'a'
            and compareA['follower_count'] > compareB['follower_count']):
        score += 1
        print(f"That is correct!, score is now: {score}")
        return True
    elif (guess == 'b'
          and compareA['follower_count'] < compareB['follower_count']):
        score += 1
        compareA = compareB
        print(f"That is correct!, score is now: {score}")
        return True

    print(f"That was incorrect, you finished with a score of {score}")
    return False


while (isRunning):
    compareB = r.choice(gd)
    guess = ''

    GameSetUp(compareA, compareB)

    while (guess != "a" and guess != "b"):
        guess = input("Which has a higher following? A or B? ")[0].lower()

    isRunning = checkGuess(compareB, guess)

    if (isRunning):
        time.sleep(0.5)
        os.system("clear")