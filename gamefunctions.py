# -*- coding: utf-8 -*-
# I think this is all what was asked for? You didn't need it in an interactive
#   format asking the user for inputs did you? 
"""
Created on Sat Feb 21 10:22:32 2026

@author: beaut
"""

# Module 6 Assignment

#welcome message

def print_welcome(name, width):
    """
    Prints a welcome message for the input name centered
    within a field of the specified width.
    """
    message = f"Hello, {name}!"
    print(f"{message:^{width}}")

print_welcome("Jim", 1)
print()
print_welcome('Jimmy', 20)
print()
print_welcome("Jimmer", 40)
print()
print()

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

print_shop_menu("Headly", 0.10, "New Sheriff", 1.234)
print()

print_shop_menu("Austen P. ", 300, "Mini-Me", 30.3030)
print()

print_shop_menu("Lightsaber", 450, "Sword", 20)
print()





# Module 5 Assignment - coded out with docstrings for simplicity.

# Happy to resubmit without the docstrings if desired
'''
import random

def purchase_item(itemPrice, startingMoney, quantityToPurchase=1): #the =1 sets default quantity to one
    max_num_purchase = startingMoney // itemPrice
    num_purchased = min(quantityToPurchase, max_num_purchase)
    money_remaining = startingMoney - (num_purchased * itemPrice)
    return num_purchased, money_remaining
    
startingMoney = 500

lightsaber = 450
quantityToPurchase = 1000
num_purchased, money_remaining = purchase_item(lightsaber, startingMoney, quantityToPurchase)
print(f'Starting Money: ${startingMoney}')
print("Item purchased: Lightsaber")
print(f'Number purchased: {num_purchased}')
print(f"Money remaining: ${money_remaining}\n")


sword = 20
quantityToPurchase = 2
num_purchased, money_remaining = purchase_item(sword, startingMoney, quantityToPurchase)
print(f'Starting Money: ${startingMoney}')
print('Item purchased: Sword')
print(f'Number purchased: {num_purchased}')
print(f"Money remaining: ${money_remaining}\n")

AustenPowers = 300
num_purchased, money_remaining = purchase_item(AustenPowers, startingMoney)
print(f'Starting Money: ${startingMoney}')
print('Accomplace purchased: Austen Powerovich')
print(f'Number purchased: {num_purchased}')
print(f"Money remaining: ${money_remaining}\n")

print("And now... there be monsters\n")




def new_random_monster():
    
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


m1 = new_random_monster()
print(m1['name'])
print(m1['description'])
print(f'Health: {m1['health']}')
print(f'Power: {m1['power']}')
print(f'Financial Resources: {m1['money']}')
print()

m2 = new_random_monster()
print(m2['name'])
print(m2['description'])
print(f'Health: {m2['health']}')
print(f'Power: {m2['power']}')
print(f'Financial Resources: {m2['money']}')
print()

m3 = new_random_monster()
print(m3['name'])
print(m3['description'])
print(f'Health: {m3['health']}')
print(f'Power: {m3['power']}')
print(f'Financial Resources: {m3['money']}')
print()


'''















