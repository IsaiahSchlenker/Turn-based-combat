class Character(object):
    def __init__(self):
        super().__init__()
        
        self.name = "Obama"
        self.hitPoints = 100
        self.hitChance = 10
        self.maxDamage = 1000
        self.armor = 10
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
            self.__name = value
            
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
    
    @property
    def maxDamage(self):
        return self.__maxDamage
    
    @hitPoints.setter
    def maxDamage(self, value):
        if type(value) == int:
            if value >= 0:
                self.__maxDamage = value
            else:
               print("damage must be positive")
               self.__maxDamage = 1
        else:
            print("damage must be a number")
            self.__maxDamage = 1
        return self.__maxDamage
    @property
    def armor(self):
        return self.__armor
    
    @armor.setter
    def armor(self, value):
        if type(value) == int:
            if value >= 0:
                self.armor = value
            else:
               print("armor must be positive")
               self.armor = 1
        else:
            print("armor must be a number")
            self.armor = 1
            
    def printStats(self):
        print(f"""{self.name}
        Hit Points: {self.hitPoints}
        Hit Chance: {self.hitChance}
        Max Damage: {self.maxDamage}
        armor:      {self.armor}""")
        
def main():
    c = Character()
    c.printStats()
    
main()
