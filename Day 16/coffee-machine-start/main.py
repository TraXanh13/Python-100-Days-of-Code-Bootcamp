from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import time

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


def run():
    choice = input(f"What would you like? ({menu.get_items()}): ").lower()

    if choice == "off":
        print("\nShutting down...\n")
        time.sleep(1)
        return
    elif choice == "report":
        print("\n~~~ REPORT ~~~\n")
        coffee_maker.report()
        money_machine.report()
        print("\n~~~~~~~~~~~~~~\n")
    else:
        drink = menu.find_drink(choice)

        if (drink is not None):
            if (coffee_maker.is_resource_sufficient(drink)):
                if (money_machine.make_payment(drink.cost)):
                    coffee_maker.make_coffee(drink)

    run()


run()
