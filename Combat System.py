# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 11:50:22 2024

@author: bluet
"""

import tbc

def main():
    keepGoing = True
    hero = tbc.Character()
    hero.name = "Hero"
    hero.hitPoints = 10
    hero.hitChance = 50
    hero.maxDamage = 5
    hero.armor = 2

    monster = tbc.Character("Monster", 20, 30, 5, 0)

    hero.printStats()
    monster.printStats()
    while keepGoing:
        tbc.fight(hero, monster)
        tbc.gameEnder(hero)
        tbc.gameEnder(monster)
        input("press enter to continue")

if __name__ == "__main__":
    main()