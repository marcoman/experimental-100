from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


class MyCoffeeMaker:
    def __init__(self):
        self.menu = Menu()
        self.coffee_maker = CoffeeMaker()
        self.money_machine = MoneyMachine()

    def run(self):
        is_on = True
        while is_on:
            options = self.menu.get_items()
            choice = input(f"What would you like? ({options}): ")
            if choice == "off":
                is_on = False
            elif choice == "report":
                self.coffee_maker.report()
                self.money_machine.report()
            elif choice == "refill":
                self.coffee_maker.resources["water"] = 300
                self.coffee_maker.resources["milk"] = 200
                self.coffee_maker.resources["coffee"] = 100
                self.coffee_maker.report()
            else:
                if choice == "espresso" or choice == "latte" or choice == "cappuccino":
                    drink = self.menu.find_drink(choice)
                    if self.coffee_maker.is_resource_sufficient(drink) and self.money_machine.make_payment(drink.cost):
                        self.coffee_maker.make_coffee(drink)
                else:
                    print("Invalid choice")

mycoffee = MyCoffeeMaker()

mycoffee.run()
