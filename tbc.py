class Character(object):
    def __init__(self):
        super().__init__()
        
        self.name = ""
        self.hitPoints = 100
        self.hitChance = 10
        self.maxDamage = 100
        self.armor = 10
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
            self.__name = value
            return self.__name
            
    @property
    def hitPoints(self):
        return self.__hitPoints
    
    @hitPoints.setter
    def hitPoints(self, value):
        if type(value) == int:
            if value >= 0:
                self.__hitPoints = value
            else:
               print("hit points must be positive")
               self.__hitPoints = 1
        else:
            print("hit points must be a number")
            self.__hitPoints = 1
        return self.__hitPoints
    
    @property
    def hitChance(self):
        return self.__hitChance
    
    @hitChance.setter
    def hitChance(self, value):
        if type(value) == int:
            if value >= 0:
                self.__hitChance = value
            else:
               print("hit chance must be positive")
               self.__hitChance = 1
        else:
            print("hit chance must be a number")
            self.__hitChance = 1
            return self.__hitChance
    
    @property
    def maxDamage(self):
        return self.__maxDamage
    
    @hitPoints.setter
    def maxDamage(self, value):
        if type(value) == int:
            if value >= 0:
                self.__maxDamage = value
            else:
               print("max damage must be positive")
               self.__maxDamage = 1
        else:
            print("max damage must be a number")
            self.__maxDamage = 1
        return self.__maxDamage
    @property
    def armor(self):
        return self.__armor
    
    @armor.setter
    def armor(self, value):
        if type(value) == int:
            if value >= 0:
                self.__armor = value
            else:
               print("armor must be positive")
               self.__armor = 1
        else:
            print("armor must be a number")
            self.__armor = 1
        return self.__armor
            
    def printStats(self):
        print(f"""{self.name}
        Hit Points: {self.hitPoints}
        Hit Chance: {self.hitChance}
        Max Damage: {self.maxDamage}
        armor:      {self.armor}""")
        
    def fight(self, enemy):
        import random
        if random.randint(1,100) < self.hitChance:
            damage = random.randint(1, self.maxDamage)
            damage -= enemy.armor
            if damage < 0:
                damage = 0
            enemy.hitPoints -= damage
            if enemy.armor > 0:
                print(f"The enemy got hit for {damage} damage but it's armor absorbed {enemy.armor} points")
            else:
                print(f"The enemy got hit for {damage} damage")
    def gameEnder(self):
        if self.hitPoints <= 0:
            keepGoing = False
        return keepGoing
    def Character(self, hitPoints, hitChance, maxDamage, armor):
        armor = armor(self, self.armor)
        maxDamage = maxDamage(self, self.maxDamage)
        hitChance = hitChance(self, self.hitChance)
        hitPoints = hitPoints(self, self.hitPoints)        
    
def main():
    c = Character()
    c.printStats()
    
main()
