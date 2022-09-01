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
            "coffee": 24
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
emoji = "☕"

res_water = resources["water"]
res_milk = resources["milk"]
res_coffee = resources["coffee"]

quarters = 0.25
dimes = 0.10
nickles = 0.05
pennies = 0.01


def calc_user_coins(drink_cost):
    print("Please insert coins.")
    sum_quarters = input("how many quarters?: ")
    sum_dimes = float(input("how many dims?: ")) * dimes
    sum_nickles = float(input("how many nickles?: ")) * nickles
    sum_pennies = float(input("how many pennies?: ")) * pennies
    user_coins = sum_quarters + sum_dimes + sum_nickles + sum_pennies
    if user_coins > drink_cost:
        change = user_coins - drink_cost
        print(f"Here is ${round(change, 2)} change.")
    return user_coins >= drink_cost


def get_user_choice():
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice not in ["espresso", "latte", "cappuccino"]:
        return user_choice, 0, 0, 0, 0
    else:
        milk = 0
        water = MENU[user_choice]["ingredients"]["water"]
        if "milk" in MENU[user_choice]["ingredients"]:
            milk = MENU[user_choice]["ingredients"]["milk"]
        coffee = MENU[user_choice]["ingredients"]["coffee"]
        cost = MENU[user_choice]["cost"]
        return user_choice, water, milk, coffee, cost


coffee_on = True
while coffee_on:
    user_choice, water, milk, coffee, cost = get_user_choice()
    if user_choice == "off":
        coffee_on = False
    elif user_choice == "report":
        print(f"Water: {res_water}ml\nMilk: {res_milk}ml\nCoffee: {res_coffee}g\nMoney: ${money}")
    elif user_choice not in ["espresso", "latte", "cappuccino"]:
        print("Not a valid drink, please select from the available selections")
    else:
        if res_water < water:
            print("Sorry, not enough water")
        elif res_milk < milk:
            print("Sorry, not enough milk")
        elif res_coffee < coffee:
            print("Sorry, not enough coffee")
        else:
            if calc_user_coins(cost):
                print(f"Here is your {user_choice} ☕ . Enjoy!")
                res_water -= water
                res_milk -= milk
                res_coffee -= coffee
                money += cost
            else:
                print("Sorry that's not enough money. Money refunded.")




