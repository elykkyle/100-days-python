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

money = 0.0


def print_report(res, money):
    print(f"Water: {res['water']}ml")
    print(f"Milk: {res['milk']}ml")
    print(f"Coffee: {res['coffee']}g")
    print(f"Money: ${money}")


def check_resources(order):
    """Checks if machine has enough resources to make order. Returns True or False"""
    req_water = MENU[order]['ingredients']['water']
    if 'milk' in MENU[order]['ingredients']:
        req_milk = MENU[order]['ingredients']['milk']
    else:
        req_milk = 0
    req_coffee = MENU[order]['ingredients']['coffee']
    if resources['water'] < req_water:
        print("Not enough water to make your order")
        return False
    elif resources['milk'] < req_milk:
        print("Not enough milk to make your order")
        return False
    elif resources['coffee'] < req_coffee:
        print("Not enough coffee to make your order.")
        return False
    else:
        return True


def get_money(order):
    cost = MENU[order]['cost']
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))
    total_paid = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    if total_paid >= cost:
        change = "{:.2f}".format(round(total_paid - cost, 2))
        if total_paid > cost:
            print(f"Your change is ${change}")
        return cost
    else:
        print("Sorry, that's not enough money. Money refunded.")


def make_drink(order, resources):
    remaining = {}
    remaining['water'] = resources['water'] - MENU[order]['ingredients']['water']
    remaining['coffee'] = resources['coffee'] - MENU[order]['ingredients']['coffee']
    if 'milk' in order:
        remaining['milk'] = resources['water'] - MENU[order]['ingredients']['water']
    else:
        remaining['milk'] = resources['milk']
    print(f"Here is your {order}. Enjoy!")
    return remaining



# TODO #1: Prompt user by asking 'what would you like? (espresso/latte/cappuccino)'
# TODO #2: Turn off the coffee machine by entering "off" to the prompt
# TODO #3: Print report
# TODO #4: Check resources sufficient?
# TODO #5: Process coins.
# TODO #6: Check transaction successful?
# TODO #7: Make coffee.

machine_on = True

while machine_on:
    enough_resources = False
    order = input("What would you like? (espresso/latte/cappuccino)? ")
    if order == 'off':
        machine_on = False
        break
    elif order == 'report':
        print_report(resources, money)
    else:
        enough_resources = check_resources(order)
    if enough_resources:
        money = get_money(order)
    else:
        continue
    resources = make_drink(order, resources)
