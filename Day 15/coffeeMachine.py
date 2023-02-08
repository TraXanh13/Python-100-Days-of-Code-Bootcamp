import time
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0

def getReport():
    report = "\n~~~REPORT~~~\n\n"
    report += f"Water: {resources['water']}ml\n"
    report += f"Milk: {resources['milk']}ml\n"
    report += f"Coffee: {resources['coffee']}g\n"
    report += f"Money: ${money}\n"

    return report

def checkResources(drink):
    for inge in drink["ingredients"]:
        if drink["ingredients"][inge] > resources[inge]:
            print(f"Sorry there is not enough {inge}")
            return False
    return True

def processCoins(drink):
    print(f"Cost: ${drink['cost']}")
    print("Please Insert Coins")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    total = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    if total > drink["cost"]:
        print(f"Here is ${round(total - drink['cost'], 2)} in change")
    
    return total


def start():
    global money
    choice = ""

    print("Welcome to the coffee machine")
    
    while(choice not in MENU and choice != "off" and choice != "report"):
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        print("Turning off...\n")
        time.sleep(0.5)
        return

    if choice == "report":
        print(getReport())
        start()
    
    if choice in MENU:
        if(checkResources(MENU[choice])):
            if(processCoins(MENU[choice]) >= MENU[choice]["cost"]):
                print(f"Here is your {choice}. Enjoy! ☕\n\n")
                money += MENU[choice]["cost"]
                for inge in MENU[choice]["ingredients"]:
                    resources[inge] -= MENU[choice]["ingredients"][inge]
            else:
                print("Sorry that's not enough money. Money refunded")
        start()

start()
