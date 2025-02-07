# Coffee machine // Máquina de café

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
    },
}

profit = 0 
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print("Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    print("Please insert coins. We only accept 50 centimos and higher")
    total = int(input("How many cents: ")) * 0.50
    total += int(input("How many euros: "))
    return total
    
def is_transaction_successfull(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is {change}€ in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def coffee_machine(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕︎")

is_on = True

while is_on:
    choice = input("What would you like? \n(espresso - 1.50€ / latte - 2.50€ / cappuccino - 3€ ): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: {profit}€")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successfull(payment, drink["cost"]):
                coffee_machine(choice, drink["ingredients"])
                end = input(f"Would you like something esle? Type 'yes' or 'no'. ")
                if end == "yes":
                    is_on == True
                else:
                    print("Goodbye!")
                    break