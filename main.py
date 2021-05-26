# Menu, MenuItem
from menu import*
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

print_all_report = CoffeeMaker()
print_report = MoneyMachine()
print_menu = Menu()

is_on = True

while is_on:
    options = print_menu.get_items()
    choices = input(f"What would you like? ({options}):")

    if choices == "off":
        is_on = False
    elif choices == "report":
        print_all_report.report()
        print_report.report()
    else:
        drink = print_menu.find_drink(choices)
        if print_all_report.is_resource_sufficient(drink) and print_report.make_payment(drink.cost):
            print_all_report.make_coffee(drink)