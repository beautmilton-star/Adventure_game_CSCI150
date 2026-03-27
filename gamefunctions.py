# -*- coding: utf-8 -*-
 
"""
Utility functions for a simple text-based game.

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

def print_welcome(name, width):
    """
    Print a centered welcome message.

    Parameters:
        name (str): The player's name.
        width (int): Width of the printed field.

    Returns:
        None
    """
    message = f"Hello, {name}!"
    print(f"{message:^{width}}")

def print_shop_menu(item1_name, item1_price, item2_name, item2_price):
    """
    Print a formatted shop menu with two items.

    Parameters:
        item1_name (str): Name of the first item.
        item1_price (float): Price of the first item.
        item2_name (str): Name of the second item.
        item2_price (float): Price of the second item.

    Returns:
        None
    """
    print("/----------------------\\")
    print(f"| {item1_name:<12}${item1_price:>7.2f} |")
    print(f"| {item2_name:<12}${item2_price:>7.2f} |")
    print("\\----------------------/")

def purchase_item(item_price, starting_money, quantity_to_purchase=1):
    """
    Calculate how many items can be purchased and money remaining.

    Parameters:
        item_price (int | float): Cost of one item.
        starting_money (int | float): Money available to spend.
        quantity_to_purchase (int): Desired quantity to purchase.

    Returns:
        tuple: Number purchased and money remaining.
    """
    max_num_purchase = starting_money // item_price
    num_purchased = min(quantity_to_purchase, max_num_purchase)
    money_remaining = starting_money - (num_purchased * item_price)
    return int(num_purchased), money_remaining

def random_monster():
    """
    Create and return a random monster dictionary.

    Returns:
        dict: Monster data with name, description, health, power, and money.
    """
    monster_type = random.choice(
        ["Purple People Eater", "Politician", "Dr. Evil"]
    )

    if monster_type == "Purple People Eater":
        return {
            "name": "Purple People Eater",
            "description": (
                "You come across a one-eyed, one-horned flying purple "
                "people eater. What a sight to see!"
            ),
            "health": random.randint(4, 8),
            "power": random.randint(2, 5),
            "money": random.randint(8, 15),
        }

    if monster_type == "Politician":
        return {
            "name": "Politician",
            "description": (
                "You found the most wretched of monsters. It smiles, waves, "
                "and prepares to drain your will to live."
            ),
            "health": random.randint(5, 9),
            "power": random.randint(1, 4),
            "money": random.randint(10, 18),
        }

    return {
        "name": "Dr. Evil",
        "description": (
            "He didn't spend 8 years in evil medical school to be called "
            "Mr. He attacks with sharks with laser beams attached to their heads."
        ),
        "health": random.randint(7, 11),
        "power": random.randint(3, 6),
        "money": random.randint(15, 25),
    }

def get_valid_menu_choice(min_choice, max_choice):
    """
    Prompt until the user enters a valid numeric menu choice.

    Parameters:
        min_choice (int): Lowest valid option.
        max_choice (int): Highest valid option.

    Returns:
        str: Validated menu choice.
    """
    while True:
        choice = input("> ")
        if choice.isdigit():
            number = int(choice)
            if min_choice <= number <= max_choice:
                return choice
        print("Invalid choice. Please try again.")

def display_town_menu(current_hp, current_gold):
    """
    Display the town menu.

    Parameters:
        current_hp (int): Player's current HP.
        current_gold (int): Player's current gold.

    Returns:
        None
    """
    print("\nYou are in town.")
    print(f"Current HP: {current_hp}, Current Gold: {current_gold}")
    print("What would you like to do?")
    print("1) Leave town (Fight Monster)")
    print("2) Sleep (Restore HP for 5 Gold)")
    print("3) Quit")

def sleep_in_town(current_hp, current_gold, max_hp=30, sleep_cost=5):
    """
    Restore HP if the player can afford to sleep.

    Parameters:
        current_hp (int): Player's current HP.
        current_gold (int): Player's current gold.
        max_hp (int): Maximum player HP.
        sleep_cost (int): Gold required to sleep.

    Returns:
        tuple: Updated HP and gold.
    """
    if current_gold < sleep_cost:
        print("You do not have enough gold to sleep.")
        return current_hp, current_gold

    if current_hp == max_hp:
        print("You are already at full health.")
        return current_hp, current_gold

    print("You sleep at the inn and wake up refreshed.")
    return max_hp, current_gold - sleep_cost

def display_fight_status(player_hp, monster):
    """
    Display current combat statistics and options.

    Parameters:
        player_hp (int): Player's current HP.
        monster (dict): Current monster.

    Returns:
        None
    """
    print(f"\nYou are fighting: {monster['name']}")
    print(monster["description"])
    print(f"Your HP: {player_hp}")
    print(f"{monster['name']} HP: {monster['health']}")
    print("1) Attack")
    print("2) Run Away")

def get_fight_action():
    """
    Get a validated combat action from the user.

    Returns:
        str: The user's combat choice.
    """
    return get_valid_menu_choice(1, 2)

def do_combat_round(player_hp, monster):
    """
    Resolve one round of combat.

    Parameters:
        player_hp (int): Player's current HP.
        monster (dict): Current monster.

    Returns:
        tuple: Updated player HP and monster dictionary.
    """
    player_damage = random.randint(3, 6)
    monster_damage = monster["power"]

    monster["health"] -= player_damage
    print(f"You hit the {monster['name']} for {player_damage} damage.")

    if monster["health"] > 0:
        player_hp -= monster_damage
        print(f"The {monster['name']} hits you for {monster_damage} damage.")

    return player_hp, monster

def fight_monster(player_hp, player_gold):
    """
    Run the combat loop against a random monster.

    Parameters:
        player_hp (int): Player's current HP.
        player_gold (int): Player's current gold.

    Returns:
        tuple: Updated HP and gold after combat.
    """
    monster = random_monster()

    while player_hp > 0 and monster["health"] > 0:
        display_fight_status(player_hp, monster)
        action = get_fight_action()

        if action == "1":
            player_hp, monster = do_combat_round(player_hp, monster)
        else:
            print("You ran away.")
            break

    if player_hp <= 0:
        print("Your character passed out.")
        player_hp = 0
    elif monster["health"] <= 0:
        print(f"You defeated the {monster['name']}!")
        print(f"You found {monster['money']} gold.")
        player_gold += monster["money"]

    return player_hp, player_gold

def test_functions():
    """
    Run simple test calls for earlier assignment functions.

    Returns:
        None
    """
    print_welcome("Jim", 20)
    print_welcome("Jimmy", 25)
    print_welcome("Jimmer", 30)
    print()

    print_shop_menu("Headly", 0.10, "New Sheriff", 1.234)
    print()
    print_shop_menu("Austen P.", 300, "Mini-Me", 30.3030)
    print()
    print_shop_menu("Lightsaber", 450, "Sword", 20)
    print()

    starting_money = 500

    print(purchase_item(450, starting_money, 1000))
    print(purchase_item(20, starting_money, 2))
    print(purchase_item(300, starting_money))
    print()

    for _ in range(3):
        monster = random_monster()
        print(monster)
        print()

if __name__ == "__main__":
    test_functions()














