import tbc

def main():
    keepGoing = True
    hero = tbc.Character()
    hero.name = "Hero"
    hero.hitPoints = 10
    hero.hitChance = 50
    hero.maxDamage = 5
    hero.armor = 2

    monster = tbc.Character()
    monster.name = "Monster"
    monster.hitPoints = 100
    monster.hitChance = 25
    monster.maxDamage = 5
    monster.armor = 0

    while keepGoing:
        hero.printStats()
        monster.printStats()
        health = tbc.fight(hero, monster)
        health1 = tbc.fight(monster, hero)
        if health <= 0:
            keepGoing = False
        if health1 <= 0:
            keepGoing = False
        input("press enter to continue")

if __name__ == "__main__":
    main()
