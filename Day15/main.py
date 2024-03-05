MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 15,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 25,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 30,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

is_on = True
profit = 0

def is_resource_sufficient(ordered_ingredients):
    for item in ordered_ingredients:
        if ordered_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        return True

def process_coins():
    """Return the total calculated from coins inserted."""
    print("Please input Money")
    total = int(input("Enter the money :"))

    return total


def is_transaction_sucessful(money_recieved, drink_cost):
    """Return True when the payment is accepted ,False it is insufficient"""
    if money_recieved >= drink_cost:
        change = round(money_recieved - drink_cost, 2)
        print(f"Here is ₹{change} change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Insufficient Fund,Not enough money")
        print(f"The cost of the {choice} is {drink['cost']}")
        return False

def make_cofee(drink_name,order_ingredents):
    for item in order_ingredents:
        resources[item] -= order_ingredents[item]
    print(f"Here is your {drink_name} ☕")

def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee : {resources['coffee']}g")
    print(f"Money : {profit}$")




while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice =="report":
        report()
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_sucessful(payment,drink['cost']):
                make_cofee(choice, drink['ingredients'])

