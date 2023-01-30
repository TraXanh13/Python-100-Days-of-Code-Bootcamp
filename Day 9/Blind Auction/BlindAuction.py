import os
from BlindAuctionArt import logo

bidders = {}
running = True


def findHighestBidder():
    highestBidder = ""
    highestBid = 0

    for bidder in bidders:
        if (bidders[bidder] > highestBid):
            highestBidder = bidder
            highestBid = bidders[bidder]

    print(f"The winner is {highestBidder} with a bid of ${highestBid}.")


while (running):
    print(logo)
    print("Welcome to the secret auction program.")
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))

    bidders[name] = bid

    if (input("Is there another entry? (y/n) ") == "n"):
        running = False
        findHighestBidder()
        break
    else:
        os.system("cls")
