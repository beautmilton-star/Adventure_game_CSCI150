# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 16:35:41 2026

@author: beaut
"""

import random

class WanderingMonster:
    def __init__(self, x, y, monster_type, color, hp):
        self.x = x
        self.y = y
        self.monster_type = monster_type
        self.color = list(color)  # ensure JSON safe
        self.hp = hp

    @staticmethod
    def random_spawn(occupied, forbidden, grid_w, grid_h):
        while True:
            x = random.randint(0, grid_w - 1)
            y = random.randint(0, grid_h - 1)

            if (x, y) not in occupied and (x, y) not in forbidden:
                return WanderingMonster(
                    x, y,
                    monster_type="Goblin",
                    color=[255, 0, 0],
                    hp=10
                )

    @staticmethod
    def from_dict(data):
        return WanderingMonster(
            data["x"],
            data["y"],
            data["monster_type"],
            data["color"],
            data["hp"]
        )

    def to_dict(self):
        return {
            "x": self.x,
            "y": self.y,
            "monster_type": self.monster_type,
            "color": list(self.color),
            "hp": self.hp
        }

    def move(self, occupied, forbidden, grid_w, grid_h):
        directions = [
            (0, -1),  # up
            (0, 1),   # down
            (-1, 0),  # left
            (1, 0)    # right
        ]

        dx, dy = random.choice(directions)
        new_x = self.x + dx
        new_y = self.y + dy

        if not (0 <= new_x < grid_w and 0 <= new_y < grid_h):
            return  # stay put

        if (new_x, new_y) in occupied:
            return

        if (new_x, new_y) in forbidden:
            return

        self.x = new_x
        self.y = new_y