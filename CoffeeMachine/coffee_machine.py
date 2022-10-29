import models

def print_report():
    for key in models.resources:
        print(f"{key}: {models.resources[key]}{models.measure[key]}")

def is_sufficient(coffee_type):
    coffee_reqs = models.coffee_menu[coffee_type]
    for key in models.coffee_menu[coffee_type]:
        if key != "cost" and (models.resources[key] < coffee_reqs[key]):
            print(f"Sorry there is not enough {key}.")
            return False
    return True

def calculate_value(quarter, dime, nickle, penny):
    return ((quarter * models.coin_value["quarter"]) +
        (dime * models.coin_value["dime"]) + 
        (nickle * models.coin_value["nickle"]) +
        (penny * models.coin_value["penny"]))

def collect_money():
    quarter = int(input("How many quarters? "))
    dime = int(input("How many dime? "))
    nickle = int(input("How many nickle? "))
    penny = int(input("How many penny? "))

    return calculate_value(quarter, dime, nickle, penny)

def update_resources(coffee_type):
    for key in models.coffee_menu[coffee_type]:
        if key == "cost":
            continue
        models.resources[key] -= models.coffee_menu[coffee_type][key]

    models.resources["money"] += models.coffee_menu[coffee_type]["cost"]


def make_coffee():
    coffee_requested = input("What would you like? (espresso/latte/cappuccino): ")
    if coffee_requested == "report":
        print_report()
        return

    while coffee_requested not in models.coffee_menu:
        print("Not in menu, please try again!")
        coffee_requested = input("What would you like? (espresso/latte/cappuccino): ")
    
    if not is_sufficient(coffee_requested):
        return

    money_inserted =  collect_money()
    if money_inserted < models.coffee_menu[coffee_requested]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return
    
    update_resources(coffee_requested)

    print(f"Here is your {coffee_requested}. Enjoy!")

    if money_inserted > models.coffee_menu[coffee_requested]["cost"]:
        change = money_inserted - models.coffee_menu[coffee_requested]["cost"]
        print(f"Here is ${change} dollars in change.")

while True:
    make_coffee()