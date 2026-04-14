# -*- coding: utf-8 -*-

"""Main game file that uses functions from gamefunctions.py."""

import gamefunctions

print("1) New Game")
print("2) Load Game")

start_choice = input("> ")

if start_choice == "2":
    state = gamefunctions.load_game()

    if state is None:
        name = input("Enter your character's name: ")
        state = {
            "player_name": name,
            "player_hp": 30,
            "player_max_hp": 30,
            "player_gold": 100,
            "player_inventory": [],
            "equipped_weapon": None,
            "map": {
                "player_pos": [0, 0],
                "town_pos": [0, 0],
                "monster_pos": [5, 5]
                }
            }
        
else:
    name = input("Enter your character's name: ")
    state = {
        "player_name": name,
        "player_hp": 30,
        "player_max_hp": 30,
        "player_gold": 100,
        "player_inventory": [],
        "equipped_weapon": None,
        "map": {
            "player_pos": [0, 0],
            "town_pos": [0, 0],
            "monster_pos": [5, 5]
            }
            }

choice = ""

while state["player_hp"] > 0 and choice not in ["6", "7"]:
    gamefunctions.print_character(state)

    gamefunctions.display_town_menu(state)
    choice = gamefunctions.get_valid_menu_choice(1, 7)

    if choice == "1":
        result = gamefunctions.map_interface(state)

        if result == "monster":
            state = gamefunctions.fight_monster(state)

            # Move monster after fight
            import random
            while True:
                new_pos = [random.randint(0, 9), random.randint(0, 9)]
                if new_pos != state["map"]["player_pos"] and new_pos != state["map"]["town_pos"]:
                    state["map"]["monster_pos"] = new_pos
                    break

        elif result == "town":
            pass  # just go back to menu

    elif choice == "2":
        state = gamefunctions.sleep_in_town(state)

    elif choice == "3":
        state = gamefunctions.shop_menu(state)

    elif choice == "4":
        gamefunctions.show_inventory(state)

    elif choice == "5":
        state = gamefunctions.equip_weapon(state)

    elif choice == "6":
        gamefunctions.save_game(state)
        print("Game saved. Goodbye.")
        break
        
    elif choice == "7":
        print("Goodbye.")
        break
    
    else:
        print("Invalid choice.")

if state["player_hp"] <= 0:
    print("You have died. Game over.")