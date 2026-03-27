# -*- coding: utf-8 -*-

"""Main game file that uses functions from gamefunctions.py."""

import gamefunctions


# -*- coding: utf-8 -*-
"""Main game file that runs the town game loop."""

import gamefunctions

def main():
    """Run the main game loop."""
    name = input("Enter your name: ")
    gamefunctions.print_welcome(name, 30)

    hp = 30
    gold = 10

    while True:
        gamefunctions.display_town_menu(hp, gold)
        choice = gamefunctions.get_valid_menu_choice(1, 3)

        if choice == "1":
            hp, gold = gamefunctions.fight_monster(hp, gold)
        elif choice == "2":
            hp, gold = gamefunctions.sleep_in_town(hp, gold)
        else:
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()