from data import MENU, resources

# Initialize variables
change = 0
till_amount = 0
coffee_option = ''


def print_report():
    """
    Prints the remaining resources.
    :return: None
    """

    # Print report
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${till_amount}")


def check_resources(ordered_ingredients):
    """
    Checks if resources are sufficient for the order.
    :param ordered_ingredients: dictionary with ingredients
    :return: Boolean
    """

    for ingredient in ordered_ingredients:
        if ordered_ingredients[ingredient] > resources[ingredient]:
            return False, ingredient
        else:
            return True, ''


def calculate_coins():
    """
    Calculates total amount from the coins.
    :return: int - total amount
    """

    print("Please insert coins.")

    how_many = "How many"
    quarters = int(input(f"{how_many} quarters?: "))
    dimes = int(input(f"{how_many} dimes?: "))
    nickels = int(input(f"{how_many} nickels?: "))
    pennies = int(input(f"{how_many} pennies?: "))

    return quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01


def calculate_change(paid, price):
    """
    Calculate change from the amount.
    :param paid: paid amount
    :param price: coffee amount
    :return: int - transaction change
    """

    return paid - price


def update_resources(ingredients):
    """
    Updating the resources and money.
    :param ingredients: dictionary - chosen coffee ingredients
    :return: None
    """

    for ingredient in ingredients:
        resources[ingredient] -= ingredients[ingredient]


while True:
    user_option = input("What would you like? (espresso/latte/cappuccino): ")

    if user_option == "report":
        print_report()
    elif user_option == "off":
        break
    else:
        # Assign coffee option
        coffee_option = user_option

        # Check if resources available
        is_resources_available, not_enough_resource = check_resources(MENU[coffee_option]["ingredients"])

        # Calculate amount from coins
        amount = calculate_coins()

        # Check if amount is enough
        is_amount_enough = amount >= MENU[coffee_option]["cost"]

        if is_resources_available and is_amount_enough:
            # Calculate change
            change = calculate_change(amount, MENU[coffee_option]["cost"])

            if change:
                print(f"Here is ${change} in change.")

            print(f"Here is your {coffee_option} ☕ Enjoy!")

            # Update resources
            update_resources(MENU[user_option]['ingredients'])
            till_amount += amount
        elif is_resources_available and not is_amount_enough:
            print("Sorry that's not enough money. Money refunded.")
        elif not is_resources_available:
            print(f"Sorry there is not enough {not_enough_resource}")
