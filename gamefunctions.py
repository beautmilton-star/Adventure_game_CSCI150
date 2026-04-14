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
import json
from WanderingMonster import WanderingMonster

def save_game(state, filename="savegame.json"):
    state_copy = state.copy()

    # convert monsters to dicts
    state_copy["monsters"] = [m.to_dict() for m in state["monsters"]]

    with open(filename, "w") as f:
        json.dump(state_copy, f, indent=4)

    print(f"Game saved to {filename}")

def load_game(filename="savegame.json"):
    """Load game state from JSON file."""
    try:
        with open(filename, "r") as f:
            state = json.load(f)
            
        if "monsters" in state:
            state["monsters"] = [
                WanderingMonster.from_dict(m)
                for m in state["monsters"]
            ]
        print(f"Game loaded from {filename}")
        return state
    except FileNotFoundError:
        print("Save file not found. Starting new game.")
        return None

def print_character(state):
    print("\n--- CHARACTER ---")
    print(f"Name: {state['player_name']}")
    print(f"HP: {state['player_hp']}")
    print(f"Gold: {state['player_gold']}")
    print("-----------------\n")

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


def display_town_menu(state):
    
    print("\nYou are in town.")
    print(f"Current HP: {state['player_hp']}, Current Gold: {state['player_gold']}")
    print("What would you like to do?")
    print("1) Explore (Find Monster Or Return to Town)")
    print("2) Sleep (Restore HP for 5 Gold)")
    print("3) Shop")
    print("4) Inventory")
    print("5) Equip Weapon")
    print("6) Save and Quit")
    print("7) Quit Without Saving")

def sleep_in_town(state, sleep_cost=5):
    if state["player_gold"] < sleep_cost:
        print("You do not have enough gold to sleep.")
        return state

    if state["player_hp"] == state["player_max_hp"]:
        print("You are already at full health.")
        return state

    print("You sleep at the inn and wake up refreshed.")
    state["player_gold"] -= sleep_cost
    state["player_hp"] = state["player_max_hp"]
    return state

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

def do_combat_round(state, monster):
    player_damage = random.randint(3, 6)

    weapon = state["equipped_weapon"]
    if weapon:
        player_damage += weapon["damageBonus"]
        weapon["currentDurability"] -= 1

        if weapon["currentDurability"] <= 0:
            print(f"Your {weapon['name']} broke!")
            state["player_inventory"].remove(weapon)
            state["equipped_weapon"] = None

    monster_damage = monster["power"]

    monster["health"] -= player_damage
    print(f"You hit the {monster['name']} for {player_damage} damage.")

    if monster["health"] > 0:
        state["player_hp"] -= monster_damage
        print(f"The {monster['name']} hits you for {monster_damage} damage.")

    return state, monster

def fight_monster(state):
    monster = random_monster()

    while state["player_hp"] > 0 and monster["health"] > 0:
        display_fight_status(state["player_hp"], monster)

        print("3) Use Special Item")

        action = input("> ")

        if action == "1":
            state, monster = do_combat_round(state, monster)

        elif action == "2":
            print("You ran away.")
            break

        elif action == "3":
            for i, item in enumerate(state["player_inventory"]):
                if item["type"] == "special":
                    use = input("Use special item? (y/n): ")
                    if use == "y":
                        state["player_inventory"].pop(i)
                        print("Monster instantly defeated!")
                        state["player_gold"] += monster["money"]
                        return state
                    break
            else:
                print("No special items.")

    if state["player_hp"] <= 0:
        state["player_hp"] = 0

    elif monster["health"] <= 0:
        print(f"You defeated the {monster['name']}!")
        print(f"You found {monster['money']} gold.")
        state["player_gold"] += monster["money"]

    return state


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

def shop_menu(state):
    while True:
        print("\n--- SHOP ---")
        print(f"Gold: {state['player_gold']}")
        print("1. Sword (25 gold)")
        print("2. Magic Bomb (15 gold)")
        print("3. Leave")

        choice = input("> ")

        if choice == "1":
            if state["player_gold"] >= 25:
                state["player_inventory"].append({
                    "name": "sword",
                    "type": "weapon",
                    "damageBonus": 3,
                    "maxDurability": 5,
                    "currentDurability": 5,
                    "equipped": False
                })
                state["player_gold"] -= 25
                print("Bought sword.")
            else:
                print("Not enough gold.")

        elif choice == "2":
            if state["player_gold"] >= 15:
                state["player_inventory"].append({
                    "name": "magic bomb",
                    "type": "special"
                })
                state["player_gold"] -= 15
                print("Bought magic bomb.")
            else:
                print("Not enough gold.")

        elif choice == "3":
            return state

def show_inventory(state):
    print("\n--- INVENTORY ---")

    if not state["player_inventory"]:
        print("Empty.")
        return

    for i, item in enumerate(state["player_inventory"], 1):
        line = f"{i}. {item['name']} ({item['type']})"

        if item["type"] == "weapon":
            line += f" | Durability {item['currentDurability']}/{item['maxDurability']}"
            if item.get("equipped"):
                line += " [EQUIPPED]"

        print(line)

def equip_weapon(state):
    weapons = [
        item for item in state["player_inventory"]
        if item["type"] == "weapon" and item["currentDurability"] > 0
    ]

    if not weapons:
        print("No usable weapons.")
        return state

    print("\nChoose weapon:")
    print("0. None")

    for i, w in enumerate(weapons, 1):
        print(f"{i}. {w['name']}")

    choice = input("> ")

    if not choice.isdigit():
        return state

    choice = int(choice)

    if choice == 0:
        state["equipped_weapon"] = None
        return state

    if 1 <= choice <= len(weapons):
        selected = weapons[choice - 1]

        for item in state["player_inventory"]:
            if item["type"] == "weapon":
                item["equipped"] = False

        selected["equipped"] = True
        state["equipped_weapon"] = selected
        print(f"Equipped {selected['name']}")

    return state

def move_player(state, direction):
    x, y = state["map"]["player_pos"]

    if direction == "w":  # up
        if y > 0:
            y -= 1
    elif direction == "s":  # down
        if y < 9:
            y += 1
    elif direction == "a":  # left
        if x > 0:
            x -= 1
    elif direction == "d":  # right
        if x < 9:
            x += 1

    state["map"]["player_pos"] = [x, y]

    if [x, y] == state["map"]["town_pos"]:
        return "returned_to_town"
    
    else:
        return "moved"

def draw_map(state):
    player = state["map"]["player_pos"]
    town = state["map"]["town_pos"]

    print("\n--- MAP ---")

    for y in range(10):
        row = ""
        for x in range(10):
            if [x, y] == player:
                row += "P "
            elif [x, y] == town:
                row += "T "
            elif any(m.x == x and m.y == y for m in state["monsters"]):
                row += "M "
            else:
                row += ". "
        print(row)

def map_interface(state):
    while True:
        draw_map(state)

        print("Move with WASD (w=up, s=down, a=left, d=right)")
        move = input("> ").lower()

        if move not in ["w", "a", "s", "d"]:
            print("Invalid move.")
            continue

        result = move_player(state, move)
        
        player_pos = tuple(state["map"]["player_pos"])

        # combat check (REQUIRED by rubric)
        for monster in state["monsters"]:
            if (monster.x, monster.y) == player_pos:
                print("A monster appears!")
                return "monster"

        # move monsters AFTER player moves
        occupied_positions = [(m.x, m.y) for m in state["monsters"]]
        town_pos = tuple(state["map"]["town_pos"])

        for monster in state["monsters"]:
            other_monsters = [
                (m.x, m.y) for m in state["monsters"] if m != monster
                ]

            monster.move(
                occupied=other_monsters,
                forbidden=[player_pos, town_pos],
                grid_w=10,
                grid_h=10
                )

        if result == "returned_to_town":
            print("You returned to town.")
            return "town"



