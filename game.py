# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 23:25:18 2026

@author: beaut
"""

"""Main game file that uses functions from gamefunctions.py."""

import gamefunctions


def main():
    """Run a simple demo game using the imported module."""
    name = input("Enter your name: ")
    gamefunctions.print_welcome(name, 30)
    print()

    gamefunctions.print_shop_menu("Potion", 10.00, "Sword", 25.00)
    print()

    starting_money = float(input("How much money do you have? "))
    quantity = int(input("How many potions would you like to buy? "))

    num_purchased, money_remaining = gamefunctions.purchase_item(
        10.00, starting_money, quantity
    )

    print(f"You bought {num_purchased} potion(s).")
    print(f"You have ${money_remaining} left.")
    print()

    monster = gamefunctions.random_monster()
    print("A wild monster appears!")
    print(monster["name"])
    print(monster["description"])
    print(f"Health: {monster['health']}")
    print(f"Power: {monster['power']}")
    print(f"Money: {monster['money']}")


if __name__ == "__main__":
    main()