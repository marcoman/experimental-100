import os
import sys

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

COINS = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.01,
}

PROMPT = "What would you like? (espresso/latte/cappuccino): "

class CoffeeMachine:
    money = 0.0
    user_money = 0.0
    def __init__(self):
        self.resources = resources
        self.menu = MENU
        self.prompt = PROMPT

    def prompt_user(self):
        turned_on = True
        user_input = input(self.prompt).lower()
        if user_input == "report":
            self.print_report()
        elif user_input == "off":
            turned_on = False
        elif user_input == "refill":
            self.resources["water"] = 300
            self.resources["milk"] = 200
            self.resources["coffee"] = 100
            print("Refilled.")
        elif user_input == "coins":
            self.take_coins()
        elif user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
            if self.check_resources(user_input):
                self.make_coffee(user_input)
        else:
            print("Invalid input. Please try again.")
        return turned_on

    def make_change (self, cost):
        self.money += cost
        change = self.user_money -  cost
        print(f"Here is ${change:.2f} in change.")
        self.user_money = 0.0

    def check_resources(self, drink):
        print(f"You have ${self.user_money:.2f} for a {self.menu[drink]['cost']:.2f} {drink}")
        make_drink = True
        coffee_cost = self.menu[drink]["cost"]
        if coffee_cost > self.user_money:
            print("Sorry that's not enough money. Money refunded.")
            make_drink = False
        else:
            ingredients = self.menu[drink]["ingredients"]
            for ingredient in ingredients:
                if ingredients[ingredient] > self.resources[ingredient]:
                    print(f"Sorry, there is not enough {ingredient}.")
                    make_drink = False
        return make_drink

    def make_coffee(self, drink):
        print (f'making {drink}...\n')
        ingredients = self.menu[drink]["ingredients"]
        for ingredient in ingredients:
            self.resources[ingredient] -= ingredients[ingredient]
        self.make_change(self.menu[drink]["cost"])
        print(f"Here is your {drink} ☕， Enjoy!")

    def take_coins(self):
        print("Please insert coins.")
        for coin in COINS:
            coins = int(input(f"How many {coin}? "))
            self.user_money += coins * COINS[coin]
        print(f"You have inserted ${self.user_money:.2f}. Thank you")
        
    def print_report(self):
        print (f"Water: {resources['water']}ml")
        print (f"Milk: {resources['milk']}ml")
        print (f"Coffee: {resources['coffee']}g")
        print (f"Money: ${self.money:.2f}")
        return True
    

    def work(self):
        self.print_report()
        turned_on = True
        while turned_on:
            turned_on = self.prompt_user()


myCoffee = CoffeeMachine()

myCoffee.work()


