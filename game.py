# -*- coding: utf-8 -*-

"""Main game file that uses functions from gamefunctions.py."""

import gamefunctions

name = input("Enter your character's name: ")

state = {
    "player_name": name,
    "player_hp": 30,
    "player_max_hp": 30,
    "player_gold": 100,
    "player_inventory": [],
    "equipped_weapon": None
}

choice = ""

while state["player_hp"] > 0 and choice != "6":
    gamefunctions.print_character(state)

    gamefunctions.display_town_menu(state)
    choice = input("> ")

    if choice == "1":
        state = gamefunctions.fight_monster(state)

    elif choice == "2":
        state = gamefunctions.sleep_in_town(state)

    elif choice == "3":
        state = gamefunctions.shop_menu(state)

    elif choice == "4":
        gamefunctions.show_inventory(state)

    elif choice == "5":
        state = gamefunctions.equip_weapon(state)

    elif choice == "6":
        print("Goodbye.")

if state["player_hp"] <= 0:
    print("You have died. Game over.")