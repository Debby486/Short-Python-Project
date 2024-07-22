# Dunder methods
# class Mage:
#     def __init__(self, health, mana):  #self is an instance of the class and its always default
#         self.is_health = health
#         self.is_mana = mana
#         print('Mage was created')
#         print(self.is_health)

#     def __len__(self): #takes just one argument and always has a return
#         return self.is_mana

# mage = Mage(100, 200)
# print(len(mage))



# inheritance
class Human:
    def __init__(self, health):
        self.health = health
    
    def attack(self):
        print('attack')

class Warrior(Human):
    def __init__(self, health, defense):
        super().__init__(health)  #super here calls the parent health
        self.defense = defense

class Barbarian(Human):
    def __init__(self, health, damage):
        super().__init__(health)
        self.damage = damage

warrior = Warrior(50, 5.5)
barbarian = Barbarian(100, 8.1)
# warrior.attack()
# barbarian.attack()
print(warrior.health)