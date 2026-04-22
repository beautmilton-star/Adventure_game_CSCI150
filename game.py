# -*- coding: utf-8 -*-

"""Main game file that uses functions from gamefunctions.py."""

import gamefunctions
from WanderingMonster import WanderingMonster

print("1) New Game")
print("2) Load Game")

start_choice = input("> ")

if start_choice == "2":
    state = gamefunctions.load_game()
    if state is not None:
        state["mountains"] = [(3,3), (3,4), (3,5)]
        state["pits"] = [(6,6), (2,7)]

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
                "town_pos": [0, 0]
            }
        }
        state["mountains"] = [(3,3), (3,4), (3,5)]
        state["pits"] = [(6,6), (2,7)]
        
        # initialize monsters for new game
        state["monsters"] = [
            WanderingMonster.random_spawn(
                occupied=[],
                forbidden=[tuple(state["map"]["town_pos"])],
                grid_w=10,
                grid_h=10
            )
        ]

    else:
        # handle loading old save that DOESN'T have monsters yet
        if "monsters" not in state:
            state["monsters"] = [
                WanderingMonster.random_spawn(
                    occupied=[],
                    forbidden=[tuple(state["map"]["town_pos"])],
                    grid_w=10,
                    grid_h=10
                )
            ]

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
            "town_pos": [0, 0]
        }
    }
    state["mountains"] = [(3,3), (3,4), (3,5)]
    state["pits"] = [(6,6), (2,7)]
    # initialize monsters for new game
    state["monsters"] = [
        WanderingMonster.random_spawn(
            occupied=[],
            forbidden=[tuple(state["map"]["town_pos"])],
            grid_w=10,
            grid_h=10
        )
    ]

choice = ""

while state["player_hp"] > 0 and choice not in ["6", "7"]:
    gamefunctions.print_character(state)

    gamefunctions.display_town_menu(state)
    choice = gamefunctions.get_valid_menu_choice(1, 7)

    if choice == "1":
        result = gamefunctions.map_interface(state)
        
        if result == "dead":
            break

        if result == "monster":
            state = gamefunctions.fight_monster(state)
            player_pos = tuple(state["map"]["player_pos"])

        # remove defeated monster
            state["monsters"] = [
                m for m in state["monsters"]
                if (m.x, m.y) != player_pos
                ]

        # respawn if none left
            if len(state["monsters"]) == 0:
                for _ in range(2):
                    new_monster = WanderingMonster.random_spawn(
                        occupied=[(m.x, m.y) for m in state["monsters"]],
                        forbidden=[tuple(state["map"]["town_pos"])],
                        grid_w=10,
                        grid_h=10
                        )
                    state["monsters"].append(new_monster)
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