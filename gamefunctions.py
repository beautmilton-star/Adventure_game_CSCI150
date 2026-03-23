# -*- coding: utf-8 -*-
 
"""
Created on Sat Feb 21 10:22:32 2026

@author: beaut
"""

"""Utility functions for a simple text-based game.

This module contains helper functions for displaying welcome messages,
printing a shop menu, purchasing items, and generating a random monster.
It is designed to be imported into another file, such as game.py.

Functions:
    print_welcome(name, width)
    print_shop_menu(item1_name, item1_price, item2_name, item2_price)
    purchase_item(item_price, starting_money, quantity_to_purchase=1)
    random_monster()

Typical usage example:
    import gamefunctions

    gamefunctions.print_welcome("Beau", 20)
    monster = gamefunctions.random_monster()
    print(monster["name"])
"""

import random


#game functions

def print_welcome(name, width):
    """
    Prints a welcome message for the input name centered
    within a field of the specified width.
    
    Parameters:
        name (str): The player's name.
        width (int): The width of the printed field.

    Returns:
        None
    """
    message = f"Hello, {name}!"
    print(f"{message:^{width}}")
    
#print shop
def print_shop_menu(item1Name, item1Price, item2Name, item2Price):
    """
    Prints a formatted shop menu displaying two items and prices.
    Item names are left-aligned and prices right-aligned with
    two decimal places inside a bordered sign.
    
    Parameters:
        item1Name (str)
        item1Price (float)
        item2Name (str)
        item2Price (float)
        
    Returns:
        None
    """
    print("/----------------------\\")
    print(f"| {item1Name:<12}${item1Price:>7.2f} |")
    print(f"| {item2Name:<12}${item2Price:>7.2f} |")
    print("\\----------------------/")

def purchase_item(itemPrice, startingMoney, quantityToPurchase=1): #the =1 sets default quantity to one
    """
    Calculate how many items can be purchased and how much money remains.

    Parameters:
        item_price (float): The cost of one item.
        starting_money (float): The amount of money available.
        quantity_to_purchase (int): The number of items requested.
            Defaults to 1.

    Returns:
        tuple: A tuple containing:
            num_purchased (int): The number of items actually purchased.
            money_remaining (float): The amount of money left after purchase.
            """
    max_num_purchase = startingMoney // itemPrice
    num_purchased = min(quantityToPurchase, max_num_purchase)
    money_remaining = startingMoney - (num_purchased * itemPrice)
    return num_purchased, money_remaining

def random_monster():
    
    monster_type = random.choice(["Purple People Eater", "Politician", "Dr. Evil"])
    
    if monster_type == "Purple People Eater":
        return{
            "name" : "Purple People Eater",
            "description" : "You came accross a one-eyed, one-horned flying purple people eater. What a sight to see!", 
            "health" : random.randint(1,6),
            "power" : random.randint(1,6),
            "money" : 50
            }
    
    elif monster_type == "Politician": 
        return{
            "name" : "Politician",
            "description" : "You found the most wretched of monsters", 
            "health" : random.randint(1,6),
            "power" : random.randint(1,6),
            "money" : 500000
            }

    elif monster_type == "Dr. Evil": 
        return{
            "name" : "Dr. Evil",
            "description" : "He didn't spend 8 years in evil medical school to be called Mr.", 
            "health" : random.randint(1,6),
            "power" : random.randint(1,6),
            "money" : "One hundred, billion, gagillion dollars... and sharks with laser beams attached to their heads!"
            }
 
def test_functions():
    print_welcome("Jim", 1)
    print()
    print_welcome("Jimmy", 20)
    print()
    print_welcome("Jimmer", 40)
    print()
    print()

    print_shop_menu("Headly", 0.10, "New Sheriff", 1.234)
    print()

    print_shop_menu("Austen P.", 300, "Mini-Me", 30.3030)
    print()

    print_shop_menu("Lightsaber", 450, "Sword", 20)
    print()

    starting_money = 500

    num_purchased, money_remaining = purchase_item(450, starting_money, 1000)
    print(f"Starting Money: ${starting_money}")
    print("Item purchased: Lightsaber")
    print(f"Number purchased: {num_purchased}")
    print(f"Money remaining: ${money_remaining}\n")

    num_purchased, money_remaining = purchase_item(20, starting_money, 2)
    print(f"Starting Money: ${starting_money}")
    print("Item purchased: Sword")
    print(f"Number purchased: {num_purchased}")
    print(f"Money remaining: ${money_remaining}\n")

    num_purchased, money_remaining = purchase_item(300, starting_money)
    print(f"Starting Money: ${starting_money}")
    print("Item purchased: Austen Powerovich")
    print(f"Number purchased: {num_purchased}")
    print(f"Money remaining: ${money_remaining}\n")

    print("And now... there be monsters\n")

    for _ in range(3):
        monster = random_monster()
        print(monster["name"])
        print(monster["description"])
        print(f"Health: {monster['health']}")
        print(f"Power: {monster['power']}")
        print(f"Financial Resources: {monster['money']}")
        print()


if __name__ == "__main__":
    test_functions()















